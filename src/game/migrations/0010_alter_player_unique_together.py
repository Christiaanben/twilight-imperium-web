# Generated by Django 4.1.3 on 2022-12-31 10:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0009_rename_users_player_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='player',
            unique_together={('user', 'lobby'), ('lobby', 'race'), ('lobby', 'color')},
        ),
    ]
