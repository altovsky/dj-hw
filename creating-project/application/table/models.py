from django.db import models

# Create your models here.


class TableSettings(models.Model):
    name = models.CharField(max_length=96, verbose_name='Имя')
    width = models.IntegerField(default=1, verbose_name='Ширина')
    index = models.IntegerField(unique=True, verbose_name='Порядковый номер')

    class Meta:
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'
        ordering = ['index']

    def __str__(self):
        return f'{self.name}'


class CSVPath(models.Model):
    path = models.FilePathField(path='/', match='.+\.csv$', recursive=True)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.pk = 1
        self.path = path
        self.save()

    class Meta:
        verbose_name = 'Путь'
        verbose_name_plural = 'Путь'
