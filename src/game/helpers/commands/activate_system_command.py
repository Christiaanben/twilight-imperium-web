from app.settings import logger
from game.models.game import Game
from game.models.player import Player
from .command import Command

class ActivateSystemCommand(Command):

    def __init__(self, system_id: int):
        self.system_id = system_id

    def execute(self, game: Game, player: Player):
        logger.info(f"Activate system: {self.system_id} for player: {player} in game: {game}")
        return [
            {
                'type': 'activate_system',
                'kwargs': {}
            }
        ]
