from django.db import models


class Player(models.Model):

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return str(self.pk)


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
    the_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player_attempts = models.IntegerField(verbose_name='Число попыток', default=0)
    players = models.ManyToManyField(
        Player,
    )

    class Meta:
        verbose_name = 'Статистика игры'
        verbose_name_plural = 'Статистика игр'
