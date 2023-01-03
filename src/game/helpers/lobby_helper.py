from channels.db import database_sync_to_async

from app.settings import logger
from game.helpers import board_helper
from game.models import Player, Game, System
from game.serializers import PlayerSerializer, GameSerializer


@database_sync_to_async
def handle_new_or_returning_player(user_id: str, game_id: str):
    """
    If the user is new to the lobby, add them to the Game (if there's space) and let everyone know.
    Else do nothing.
    """
    logger.info(f'handle_new_or_returning_player user_id: {user_id}; game_id: {game_id}')
    # TODO: check space / game already started
    player, created = Player.objects.get_or_create(game_id=game_id, user_id=user_id)
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


@database_sync_to_async
def handle_update_player(user_id: str, player_kwargs):
    logger.info(f"handle_update_player user_id: {user_id}; player_kwargs: {player_kwargs}")
    player = Player.objects.get(id=player_kwargs['id'])
    serializer = PlayerSerializer(player, data=player_kwargs)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return [
        {
            'type': 'update_player',
            'kwargs': {
                'player': serializer.data
            }
        }
    ]


@database_sync_to_async
def handle_new_game(game_id: str):
    game = Game.objects.get(id=game_id)
    board_helper.generate_board(game)
    return [{
        'type': 'new_game',
        'kwargs': {
            'game': GameSerializer(game).data
        }
    }]
