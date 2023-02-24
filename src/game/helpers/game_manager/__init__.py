from app.settings import logger
from game.models import Game, Player


def start_game(game_id: str):
    logger.info(f'Starting a new game for {game_id}')
    game = Game.objects.get(id=game_id)
    speaker = _determine_speaker(game)
    # board_helper.generate_board(game)
    # GameConsumer.create_new_game(game_id)


def _determine_speaker(game: Game) -> Player:
    if game.speaker is None:
        game.speaker = game.players.order_by('?').first()
        game.save()
    return game.speaker
