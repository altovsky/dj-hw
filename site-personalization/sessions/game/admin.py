from django.contrib import admin

from .models import Player, Game, PlayerGameInfo


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    ordering = ['-pk']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number', 'game_state')
    ordering = ['-pk']


@admin.register(PlayerGameInfo)
class PlayerGameInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'player_attempts')
    pass
