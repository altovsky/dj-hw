import random
from django.shortcuts import render
from .models import Game, Player, PlayerGameInfo
from django.conf import settings

GAME_CREATED = 0
GAME_STARTED = 1
GAME_COMPLETED = 2

template_name = 'home.html'
context = {}


def start_new_game(request):
    new_game = Game(number=int(random.uniform(1, settings.RANDOM_NUMBER_RANGE)))
    new_game.save()

    context['Who'] = 'Вы создатель игры.'
    context['number'] = new_game.number
    context['player_attempts'] = 0
    context['is_creator'] = True
    context['is_over'] = False

    request.session['game_creator'] = True
    request.session['game_identifier'] = new_game.pk


def get_second_player(request):
    current_game = Game.objects.get(game_state=GAME_CREATED)
    game_player = Player.objects.get(pk=request.session['player_id'])
    pgi = PlayerGameInfo(the_game=current_game)
    pgi.save()
    pgi.players.add(game_player)

    request.session['game_creator'] = False
    request.session['game_identifier'] = current_game.pk

    context['Who'] = f'Угадайте число от 1 до {settings.RANDOM_NUMBER_RANGE}'
    context['is_creator'] = False
    context['is_over'] = False
    context['player_attempts'] = 0


def get_creator_context(request, gm):
    context['Who'] = 'Вы создатель игры.'
    context['is_creator'] = True
    context['number'] = gm.number

    # Если текущая игра завершена
    if gm.game_state == GAME_COMPLETED:
        del request.session['game_creator']
        del request.session['game_identifier']
        context['is_over'] = True

    else:
        context['is_over'] = False


def get_second_player_context(request, gm, p_g_info):
    context['Who'] = f'Угадайте число от 1 до {settings.RANDOM_NUMBER_RANGE}'
    context['is_creator'] = False

    if request.method == 'GET':
        # 'Второй игрок начинает игру'
        gm.game_state = GAME_STARTED
        gm.save()

        context['is_creator'] = False
        context['is_over'] = False
        context['player_attempts'] = 0

    # Если очередная попытка
    elif request.method == 'POST':
        p_g_info.player_attempts += 1
        p_g_info.save()
        context['player_attempts'] = p_g_info.player_attempts

        # Если угадали число
        if int(request.POST['guessing_number']) == gm.number:
            # то завершаем игру
            del request.session['game_creator']
            del request.session['game_identifier']
            context['game_message'] = 'Вы угадали загаданное число!'
            gm.game_state = GAME_COMPLETED
            gm.save()
            context['is_over'] = True

        # Если число меньше
        elif int(request.POST['guessing_number']) < gm.number:
            context['game_message'] = 'Введенное число меньше угадываемого.'
            context['is_over'] = False

        # Если число больше
        else:
            context['game_message'] = 'Введенное число больше угадываемого.'
            context['is_over'] = False


def show_home(request):

    # Если нет такого пользователя, то создаем
    if 'player_id' not in request.session:
        new_player = Player()
        new_player.save()
        request.session['player_id'] = new_player.pk

    # Если пользователь еще не в игре
    if 'game_identifier' not in request.session:

        try:
            # Ищем уже созданную игру, к которой можно присоединиться
            current_game = Game.objects.get(game_state=GAME_CREATED)

        except Game.DoesNotExist:
            # Если нет уже созданной игры, к которой можно присоединиться, то создаем новую игру
            start_new_game(request)

        else:
            # Тогда присоединяем к игре второго игрока
            get_second_player(request)

        finally:
            request.session.save()

    else:
        gm = Game.objects.get(pk=request.session['game_identifier'])

        # Проверяем, начал ли второй игрок играть и смотроим попытки
        try:
            p_g_info = PlayerGameInfo.objects.get(the_game=request.session['game_identifier'])

        # Попадаем в этот except, если первый игрок (создатель) создал игру,
        # но второй игрок еще не присоединился к игре и PlayerGameInfo еще не записан
        # И в этот момент первый игрок (создатель) зачем-то :-) обновляет страницу.
        except PlayerGameInfo.DoesNotExist:
            context['player_attempts'] = 0

        else:
            context['player_attempts'] = p_g_info.player_attempts

        # Если создатель игры
        if request.session['game_creator']:
            get_creator_context(request, gm)

        # Тогда это второй игрок
        else:
            get_second_player_context(request, gm, p_g_info)

    return render(
        request,
        template_name,
        context,
    )
