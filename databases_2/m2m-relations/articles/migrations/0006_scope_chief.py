# Generated by Django 2.2 on 2019-04-07 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_scope_chief'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='chief',
            field=models.BooleanField(default=0, verbose_name='Основной'),
            preserve_default=False,
        ),
    ]
