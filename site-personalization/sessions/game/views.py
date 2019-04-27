import random
from django.shortcuts import render
from .models import Game, Player, PlayerGameInfo
from django.conf import settings
# from django.views.generic import TemplateView
# from .forms import HomeForm


def show_home(request):

    context = {}

    current_session = request.session
    current_session.save()
    current_player = current_session.session_key

    # Проверяем, есть ли такой пользователь
    try:
        game_player = Player.objects.get(user_session=current_player)

    # Если нет
    except Player.DoesNotExist:

        # То создаем
        new_player = Player(user_session=current_player)
        new_player.save()

    # Если пользователь еще не в игре
    if 'game_identifier' not in request.session:

        try:
            # Ищем уже созданную игру
            current_game = Game.objects.get(game_state=0)

        except Game.DoesNotExist:

            # Если нет уже созданной игры, то начинаем новую
            new_game = Game(number=random.uniform(1, settings.RANDOM_NUMBER_RANGE))
            new_game.save()

            current_session['game_creator'] = True
            current_session['game_identifier'] = new_game.pk
            request.session['game_creator'] = True
            request.session['game_identifier'] = new_game.pk

        else:
            # Значит это второй игрок

            # Сохраним второго игрока
            game_player = Player.objects.get(user_session=current_player)
            playergameinfo = PlayerGameInfo(
                play=current_game,
                second_player=game_player,
            )
            playergameinfo.save()

            current_session['game_creator'] = False
            current_session['game_identifier'] = current_game.pk
            # current_session.save()
            context['Who'] = f'Угадайте число от 1 до {settings.RANDOM_NUMBER_RANGE}'
            context['is_over'] = False

        finally:
            current_session.save()

    else:
        # Значит уже в игре
        p_g_info = PlayerGameInfo.objects.get(play=current_session['game_identifier'])
        gm = Game.objects.get(pk=current_session['game_identifier'])

        # Если создатель игры
        if request.session['game_creator']:

            context['Who'] = 'Вы создатель игры.'
            context['is_creator'] = True
            context['player_attempts'] = p_g_info.player_attempts
            context['number'] = gm.number

            if gm.game_state == 2:
                del request.session['game_creator']
                del request.session['game_identifier']
                context['is_over'] = True

            else:
                context['is_over'] = False

        # Если второй игрок
        else:

            context['Who'] = f'Угадайте число от 1 до {settings.RANDOM_NUMBER_RANGE}'
            context['is_creator'] = False

            if request.method == 'GET':
                # 'Второй игрок начинает игру'
                gm.game_state = 1
                gm.save()
                context['is_creator'] = False
                context['player_attempts'] = p_g_info.player_attempts
                context['is_over'] = False

            elif request.method == 'POST':
                p_g_info.player_attempts += 1
                p_g_info.save()
                context['player_attempts'] = p_g_info.player_attempts

                if int(request.POST['guessing_number']) == gm.number:
                    del request.session['game_creator']
                    del request.session['game_identifier']
                    context['game_massage'] = 'Вы угадали загаданное число!'
                    gm.game_state = 2
                    gm.save()
                    context['is_over'] = True

                elif int(request.POST['guessing_number']) < gm.number:
                    context['game_massage'] = 'Введенное число меньше угадываемого.'
                    context['is_over'] = False

                else:
                    context['game_massage'] = 'Введенное число больше угадываемого.'
                    context['is_over'] = False

            else:
                context['Who'] += ' Второй игрок! - не понятно...'

    ren = render(
        request,
        'home.html',
        context,
    )

    return ren
