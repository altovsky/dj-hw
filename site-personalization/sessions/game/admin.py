from django.contrib import admin

from .models import Player, Game, PlayerGameInfo


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_session')
    ordering = ['-pk']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number', 'state')
    ordering = ['-pk']


@admin.register(PlayerGameInfo)
class PlayerGameInfoAdmin(admin.ModelAdmin):
    pass
