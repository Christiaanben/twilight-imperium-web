from app.settings import logger
from .command import Command
from game.models import Game, Player


class ActivateCardCommand(Command):

    def __init__(self, card_id: str):
        self.card_id = card_id

    def execute(self, game: Game, player: Player):
        logger.info(f"Activate card: {self.card_id} for player: {player} in game: {game}")
        # TODO: implement logic
        return []
