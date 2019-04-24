from django.shortcuts import render

from .models import Game, Player, PlayerGameInfo


def show_home(request):

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
    finally:
        # Если уже есть
        print(0)

    # Если пользователь не в игре
    if 'game_identifier' not in request.session:
        try:
            # Ищем созданную игру, чтобы стать оппонентом
            opponent_play = Game.objects.get(state=0)
        except Game.DoesNotExist:
            # Если нет созданной, то начинаем новую
            new_game = Game(number=7)
            new_game.save()
            new_game_id = new_game.pk
            # Сохраняем в сессии ID игры
            current_session['game_identifier'] = new_game.id
            current_session.save()
            # Становимся создателем
            # creator_user = Player.objects.get(user_session=current_player)
            # PlayerGameInfo.creator.add(creator_user)
            print(new_game)
        finally:
            # Становимся оппонентом
            # Сохраняем в сессии ID игры
            print('Game ID (1): ', request.session['game_identifier'])
            pass
    else:
        # Если уже в игре
        pass
        # Если создатель, то выводим число и кол-во попыток оппонента
        # Если оппонент, то выводим форму и "больше-меньше"

    print('Game ID (2): ', request.session['game_identifier'])

    ren = render(
        request,
        'home.html'
    )

    return ren
