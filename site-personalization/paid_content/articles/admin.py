from django.contrib import admin

from .models import Profile, Article


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # list_display = ('user_session', 'signed')
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'paid')
    # pass
