from channels.db import database_sync_to_async

from app.settings import logger
from game.models import Player
from game.serializers import PlayerSerializer


@database_sync_to_async
def handle_new_or_returning_player(user_id: str, lobby_id: str):
    """
    If the user is new to the lobby, add them to the lobby (if there's space) and let everyone know.
    Else do nothing.
    """
    logger.info(f'handle_new_or_returning_player user_id: {user_id}; lobby_id: {lobby_id}')
    # TODO: check space / game already started
    player, created = Player.objects.get_or_create(lobby_id=lobby_id, user_id=user_id)
    if created:
        return [
            {
                'type': 'new_player',
                'kwargs': {
                    'player': PlayerSerializer(player).data
                }
            }
        ]
    return []
