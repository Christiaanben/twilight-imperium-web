from .command import Command
from ...models import Game, Player, Strategy


class SelectStrategyCommand(Command):

    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, game: Game, player: Player):
        Strategy.objects.update_or_create(game=game, type=self.strategy, defaults={'player': player})
