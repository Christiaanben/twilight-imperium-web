from game.models import Strategy, Player
from game.models.enums import StrategyType


def select_strategy(player: Player, strategy_type: StrategyType):
    strategy, _ = Strategy.objects.update_or_create(game=player.game, type=strategy_type, defaults={'player': player})
    return strategy

