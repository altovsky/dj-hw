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
    # identifier = models.IntegerField(verbose_name='Идентификатор игры')
    # creator = models.CharField(max_length=96, verbose_name='Создатель игры')
    # opponent = models.CharField(max_length=96, verbose_name='Второй игрок')
    number = models.IntegerField(verbose_name='Число')
    state = models.IntegerField(default=0, verbose_name='Код состояния')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return str(self.pk)


class PlayerGameInfo(models.Model):
    creator = models.ManyToManyField(Player, related_name='creators')
    opponent = models.ManyToManyField(Player, related_name='opponents')
    play = models.ManyToManyField(Game, related_name='games')
    # creator = models.CharField(max_length=96, verbose_name='Создатель игры')
    # number = models.IntegerField(max_length=10, verbose_name='Число')
    attempts = models.IntegerField(verbose_name='Число попыток')
