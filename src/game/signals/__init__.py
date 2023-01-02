from django.db.models.signals import pre_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync

from game.consumers.lobby_consumer import LobbyConsumer
from game.models.player import Player

@receiver(pre_save, sender=Player)
def handle_player_ready(instance: Player, **kwargs):
    is_ready_has_changed = instance.is_ready != Player.objects.filter(id=instance.id).values_list('is_ready', flat=True).last()
    if is_ready_has_changed:
        other_players = instance.lobby.players.exclude(id=instance.id)
        if instance.is_ready:
            async_to_sync(LobbyConsumer.create_new_game)(instance.lobby_id)
