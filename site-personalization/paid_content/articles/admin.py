from django.contrib import admin

from .models import Profile, Article


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'registered_user', 'signed')
    # list_display = ('pk', 'user_session', 'signed')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'paid')
