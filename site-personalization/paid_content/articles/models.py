# from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    # pass
    user_session = models.CharField(max_length=96, verbose_name='Идентификатор сессии')
    signed = models.BooleanField(default=False, verbose_name='Подписан')


class Article(models.Model):
    # pass
    title = models.CharField(max_length=96, verbose_name='Заголовок статьи')
    img = models.FileField(upload_to='docs/article/img/%Y/%m/%d/', verbose_name='URL изображения')
    text = models.TextField(verbose_name='Текст статьи')
    paid = models.BooleanField(default=False, verbose_name='Платный ресурс')

    def __str__(self):
        return self.title
