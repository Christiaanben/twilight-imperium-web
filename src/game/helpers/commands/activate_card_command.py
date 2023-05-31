from app.settings import logger
from .command import Command
from game.models import Game, Player
from game.serializers import PlayerSerializer


class ActivateCardCommand(Command):

    def __init__(self, card_id: str):
        self.card_id = card_id

    def execute(self, game: Game, player: Player):
        logger.info(f"Activate card: {self.card_id} for player: {player} in game: {game}")
        if self.card_id == 'industrial_initiative':
            player.n_trade_goods += 1
            player.save()
        return [
            {
                'type': 'update_player',
                'kwargs': PlayerSerializer(player).data
            }
        ]
