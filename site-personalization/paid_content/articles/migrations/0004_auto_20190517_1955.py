# Generated by Django 2.2 on 2019-05-17 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_auto_20190428_0643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_session',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_v',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
