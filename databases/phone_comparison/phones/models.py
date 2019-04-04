from django.db import models


# Create your models here.
class Phone(models.Model):
    name = models.TextField()
    cost = models.TextField()
    os = models.TextField()
    screen_res = models.TextField()
    camera_res = models.TextField()
    mem = models.TextField()
    processor = models.TextField()
    glonas = models.TextField(blank=True)
    beidou = models.TextField(blank=True)

    def __str__(self):

        return self.name


class Xiaomi(Phone):
    a2dp = models.TextField(blank=True)
    irda = models.TextField(blank=True)


class Motorola(Phone):
    fm_radio = models.TextField(blank=True)
    gyro = models.TextField(blank=True)


class Alcatel(Phone):
    fm_radio = models.TextField(blank=True)
    flashlight = models.TextField(blank=True)
