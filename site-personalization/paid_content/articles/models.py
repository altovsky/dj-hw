from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    registered_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    signed = models.BooleanField(default=False, verbose_name='Подписка')

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return self.registered_user.username


class Article(models.Model):
    title = models.CharField(max_length=96, verbose_name='Заголовок статьи')
    img = models.FileField(upload_to='docs/article/img/%Y/%m/%d/', verbose_name='URL изображения')
    text = models.TextField(verbose_name='Текст статьи')
    paid = models.BooleanField(default=False, verbose_name='Платный ресурс')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
