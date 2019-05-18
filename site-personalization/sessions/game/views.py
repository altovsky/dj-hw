import random
from django.shortcuts import render
from .models import Game, Player, PlayerGameInfo
from django.conf import settings


def show_home(request):

    def start_new_game():
        new_game = Game(number=int(random.uniform(1, settings.RANDOM_NUMBER_RANGE)))
        new_game.save()

        context['Who'] = 'Вы создатель игры.'
        context['number'] = new_game.number
        context['player_attempts'] = 0
        context['is_creator'] = True
        context['is_over'] = False

        request.session['game_creator'] = True
        request.session['game_identifier'] = new_game.pk

    def get_second_player():
        game_player = Player.objects.get(user_session=user_key)
        pgi = PlayerGameInfo(the_game=current_game)
        pgi.save()
        pgi.players.add(game_player)

        request.session['game_creator'] = False
        request.session['game_identifier'] = current_game.pk

        context['Who'] = f'Угадайте число от 1 до {settings.RANDOM_NUMBER_RANGE}'
        context['is_over'] = False
        context['player_attempts'] = 0

    def get_creator_context():
        context['Who'] = 'Вы создатель игры.'
        context['is_creator'] = True
        context['number'] = gm.number

        # Если текущая игра завершена
        if gm.game_state == 2:
            del request.session['game_creator']
            del request.session['game_identifier']
            context['is_over'] = True

        else:
            context['is_over'] = False

    def get_second_player_context():
        context['Who'] = f'Угадайте число от 1 до {settings.RANDOM_NUMBER_RANGE}'
        context['is_creator'] = False

        if request.method == 'GET':
            # 'Второй игрок начинает игру'
            gm.game_state = 1
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
                gm.game_state = 2
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

    template_name = 'home.html'
    current_session = request.session
    current_session.save()
    user_key = request.session.session_key
    context = {}

    # Если нет такого пользователя, то создаем
    user_profile = Player.objects.get_or_create(user_session=user_key)

    # Если пользователь еще не в игре
    if 'game_identifier' not in request.session:

        try:
            # Ищем уже созданную игру, к которой можно присоединиться
            current_game = Game.objects.get(game_state=0)

        except Game.DoesNotExist:
            # Если нельзя присоединиться к уже созданной игры, то создаем новую игру
            start_new_game()

        else:
            # Тогда присоединяем к игре второго игрока
            get_second_player()

        finally:
            request.session.save()

    else:
        gm = Game.objects.get(pk=current_session['game_identifier'])

        # Проверяем,  начал ли второй игрок играть
        try:
            p_g_info = PlayerGameInfo.objects.get(the_game=current_session['game_identifier'])

        # Попадаем в этот except, если первый игрок (создатель) создал игру,
        # но второй игрок еще не присоединился к игре и PlayerGameInfo еще не записан
        # И в этот момент первый игрок (создатель) зачем-то :-) обновляет страницу.
        except PlayerGameInfo.DoesNotExist:
            context['player_attempts'] = 0

        else:
            context['player_attempts'] = p_g_info.player_attempts

        # Если создатель игры
        if request.session['game_creator']:
            get_creator_context()

        # Тогда это второй игрок
        else:
            get_second_player_context()

    return render(
        request,
        template_name,
        context,
    )
