from app.settings import logger
from .command import Command
from game.models import Game, Player, Strategy
from game.serializers import StrategySerializer


class SelectStrategyCommand(Command):

    def __init__(self, strategy: str):
        self.strategy = strategy

    def execute(self, game: Game, player: Player):
        logger.info(f"Select strategy: {self.strategy} for player: {player} in game: {game}")
        strategy, _ = Strategy.objects.update_or_create(game=game, base_id=self.strategy, defaults={'player': player})
        return [
            {
                'type': 'select_strategy',
                'kwargs': StrategySerializer(strategy).data
            }
        ]
