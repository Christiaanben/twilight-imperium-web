# Generated by Django 4.1.4 on 2023-01-02 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_alter_player_unique_together_player_game_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lobby',
        ),
    ]
