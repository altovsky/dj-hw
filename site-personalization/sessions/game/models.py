from django.db import models


class Player(models.Model):
    user_session = models.CharField(max_length=96, verbose_name='Идентификатор сессии')

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return self.user_session


class Game(models.Model):
    """
        Game.state - состояния игры:
        0 - создана (есть создатель, оппонента нет)
        1 - начата
        2 - окончена

    """
    number = models.IntegerField(verbose_name='Число')
    game_state = models.IntegerField(default=0, verbose_name='Код состояния')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return str(self.pk)


class PlayerGameInfo(models.Model):
    play = models.ForeignKey(Game, on_delete=models.CASCADE)
    player_attempts = models.IntegerField(verbose_name='Число попыток', default=0)
    second_player = models.ManyToManyField(
        Player,
    )

    class Meta:
        verbose_name = 'Статистика игры'
        verbose_name_plural = 'Статистика игр'
