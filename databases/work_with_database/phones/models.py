from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(verbose_name=None, primary_key=True)
    name = models.TextField(verbose_name=None)
    image = models.URLField(verbose_name=None)
    price = models.IntegerField(verbose_name=None)
    release_date = models.DateField(verbose_name=None)
    lte_exists = models.BooleanField(verbose_name=None)
    slug = models.SlugField(verbose_name=None)

    def __str__(self):
        return self.name

    def get_slug(self):
        return slugify(self.name)
