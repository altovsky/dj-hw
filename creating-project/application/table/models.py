from django.db import models

# Create your models here.


class TableSettings(models.Model):
    name = models.CharField(max_length=20)
    width = models.IntegerField(default=1)
    index = models.IntegerField(unique=True)

    class Meta:
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'
        ordering = ['index']

    def __str__(self):
        return f'{self.name}'


class FilePath(models.Model):
    path = models.FilePathField(path='/', recursive=True)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.pk = 1
        self.path = path
        self.save()

    class Meta:
        verbose_name = 'Путь'
