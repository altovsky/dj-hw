# Generated by Django 2.2 on 2019-05-23 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20190523_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='user_session',
        ),
    ]
