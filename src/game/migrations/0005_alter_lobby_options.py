# Generated by Django 4.1.3 on 2022-12-12 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_player'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lobby',
            options={'default_related_name': 'lobbies', 'verbose_name': 'Lobby', 'verbose_name_plural': 'Lobbies'},
        ),
    ]
