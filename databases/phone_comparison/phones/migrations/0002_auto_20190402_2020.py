# Generated by Django 2.1.7 on 2019-04-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcatel',
            name='flashlight',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='alcatel',
            name='fm_radio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='motorola',
            name='fm_radio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='motorola',
            name='gyro',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='beidou',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='glonas',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='xiaomi',
            name='a2dp',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='xiaomi',
            name='irda',
            field=models.TextField(blank=True),
        ),
    ]