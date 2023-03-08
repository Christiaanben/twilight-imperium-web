from django.utils import timezone

from app.settings import logger
from game.models import Game, Strategy, BaseStrategy


def start_game(game_id: str):
    logger.info(f'Starting a new game for {game_id}')
    game = Game.objects.get(id=game_id)
    game.started_at = timezone.now()
    game.speaker = game.players.order_by('?').first()
    game.save()
    _create_strategies(game)
    # board_helper.generate_board(game)
    # GameConsumer.create_new_game(game_id)


def _create_strategies(game: Game):
    strategies = [Strategy(game=game, base=base) for base in BaseStrategy.objects.all()]
    Strategy.objects.bulk_create(strategies)
