from channels.db import database_sync_to_async

from game.models import Player
from game.serializers import PlayerSerializer
from user.models import User


@database_sync_to_async
def handle_new_or_returning_player(user: User, lobby_id: str):
    """
    If the user is new to the lobby, add them to the lobby (if there's space) and let everyone know.
    Else do nothing.
    """
    # TODO: check space / game already started
    player, created = Player.objects.get_or_create(lobby_id=lobby_id, user=user)
    if not created:
        return []
    return [
        {
            'type': 'new_player',
            'kwargs': {
                'player': PlayerSerializer(player).data
            }
        }
    ]
