from abc import ABC, abstractmethod
from typing import List

from game.models import Game, Player


class Command(ABC):

    @abstractmethod
    def execute(self, game: Game, player: Player) -> List:
        pass

