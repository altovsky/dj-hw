# Generated by Django 2.2 on 2019-05-17 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20190517_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='registered',
            new_name='registered_user',
        ),
    ]