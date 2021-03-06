# Generated by Django 2.2 on 2019-05-29 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FilePathField(match='.+\\.csv$', path='/', recursive=True)),
            ],
            options={
                'verbose_name': 'Путь',
            },
        ),
        migrations.CreateModel(
            name='TableSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=96, verbose_name='Имя')),
                ('width', models.IntegerField(default=1, verbose_name='Ширина')),
                ('index', models.IntegerField(unique=True, verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'Поле',
                'verbose_name_plural': 'Поля',
                'ordering': ['index'],
            },
        ),
    ]
