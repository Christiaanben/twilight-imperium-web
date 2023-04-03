from app.settings import logger
from game.models import Game, Player, System
from .command import Command

class ActivateSystemCommand(Command):

    def __init__(self, system_id: int):
        self.system_id = system_id

    def execute(self, game: Game, player: Player):
        logger.info(f"Activate system: {self.system_id} for player: {player} in game: {game}")
        system = System.objects.get(base_id=self.system_id, game=game)
        if system.activated_by.contains(player):
            logger.warning(f"System: {system} already activated by player: {player}")
            return []
        system.activated_by.add(player)
        return [
            {
                'type': 'activate_system',
                'kwargs': {}
            }
        ]
