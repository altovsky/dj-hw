# Generated by Django 2.2 on 2019-05-17 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190517_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_v',
            new_name='registered',
        ),
    ]
