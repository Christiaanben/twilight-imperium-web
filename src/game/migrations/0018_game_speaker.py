# Generated by Django 4.1.3 on 2023-02-20 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0017_game_phase_game_round_alter_player_game_strategy'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='speaker',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.player'),
        ),
    ]