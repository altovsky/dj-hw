# Generated by Django 2.2 on 2019-04-07 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_scope_chief'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='chief',
        ),
    ]
