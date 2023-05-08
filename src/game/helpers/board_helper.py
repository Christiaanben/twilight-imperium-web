from typing import List

from app.settings import logger
from game.models import Game, Player, System, BasePlanet, Planet, BaseSystem

DEFAULT_BOARDS = {
    1: [
        # CENTER
        {'base_id': 18, 'q': 0, 'r': 0},
        # RING 1
        {'base_id': None, 'q': 1, 'r': 0},
    ],
    2: [
        # CENTER
        {'base_id': 18, 'q': 0, 'r': 0},
        # RING 1
        {'base_id': 23, 'q': 1, 'r': 0},
        {'base_id': 50, 'q': 0, 'r': 1},
        {'base_id': 37, 'q': -1, 'r': 1},
        {'base_id': 32, 'q': -1, 'r': 0},
        {'base_id': 49, 'q': 0, 'r': -1},
        {'base_id': 26, 'q': 1, 'r': -1},
        # RING 2
        # No 2,0
        {'base_id': 48, 'q': 1, 'r': 1},
        {'base_id': 21, 'q': 0, 'r': 2},
        {'base_id': 29, 'q': -1, 'r': 2},
        {'base_id': 38, 'q': -2, 'r': 2},
        {'base_id': 19, 'q': -2, 'r': 1},
        # No -2,0
        {'base_id': 39, 'q': -1, 'r': -1},
        {'base_id': 42, 'q': 0, 'r': -2},
        {'base_id': 46, 'q': 1, 'r': -2},
        {'base_id': 35, 'q': 2, 'r': -2},
        {'base_id': 28, 'q': 2, 'r': -1},
        # # RING 3
        {'base_id': 41, 'q': -2, 'r': 3},
        {'base_id': None, 'q': -3, 'r': 3},  # Faction 1
        {'base_id': 30, 'q': -3, 'r': 2},
        {'base_id': 36, 'q': 2, 'r': -3},
        {'base_id': None, 'q': 3, 'r': -3},  # Faction 2
        {'base_id': 24, 'q': 3, 'r': -2},
    ],
    3: [
        # CENTER
        {'base_id': 18, 'q': 0, 'r': 0},
        # RING 1
        {'base_id': 19, 'q': 1, 'r': 0},
        {'base_id': 44, 'q': 1, 'r': -1},
        {'base_id': 22, 'q': 0, 'r': -1},
        {'base_id': 45, 'q': -1, 'r': 0},
        {'base_id': 24, 'q': -1, 'r': 1},
        {'base_id': 42, 'q': 0, 'r': 1},
        # RING 2
        {'base_id': 38, 'q': 2, 'r': 0},
        {'base_id': 25, 'q': 1, 'r': 1},
        {'base_id': 33, 'q': 0, 'r': 2},
        {'base_id': 47, 'q': -1, 'r': 2},
        {'base_id': 27, 'q': -2, 'r': 2},
        {'base_id': 26, 'q': -2, 'r': 1},
        {'base_id': 30, 'q': -2, 'r': 0},
        {'base_id': 40, 'q': -1, 'r': -1},
        {'base_id': 35, 'q': 0, 'r': -2},
        {'base_id': 23, 'q': 1, 'r': -2},
        {'base_id': 36, 'q': 2, 'r': -2},
        {'base_id': 39, 'q': 2, 'r': -1},
        # RING 3
        {'base_id': 29, 'q': 1, 'r': 2},
        {'base_id': None, 'q': 0, 'r': 3},  # Faction 1
        {'base_id': 34, 'q': -1, 'r': 3},
        {'base_id': 28, 'q': -3, 'r': 1},
        {'base_id': None, 'q': -3, 'r': 0},  # Faction 2
        {'base_id': 21, 'q': -2, 'r': -1},
        {'base_id': 50, 'q': 2, 'r': -3},
        {'base_id': None, 'q': 3, 'r': -3},  # Faction 3
        {'base_id': 31, 'q': 3, 'r': -2},
    ],
    4: [
        # CENTER
        {'base_id': 18, 'q': 0, 'r': 0},
        # RING 1
        {'base_id': 38, 'q': 1, 'r': 0},
        {'base_id': 44, 'q': 1, 'r': -1},
        {'base_id': 48, 'q': 0, 'r': -1},
        {'base_id': 45, 'q': -1, 'r': 0},
        {'base_id': 28, 'q': -1, 'r': 1},
        {'base_id': 42, 'q': 0, 'r': 1},
        # RING 2
        {'base_id': 49, 'q': 2, 'r': 0},
    ]
}


def generate_board(game: Game):
    n_players = game.players.count()
    systems = [System(game=game, **system) for system in DEFAULT_BOARDS[n_players]]
    for player, system in zip(game.players.all(), filter(lambda s: s.base_id is None, systems)):
        system.base = BaseSystem.objects.get(faction=player.faction)
    logger.info(f"Creating {len(systems)} systems")
    System.objects.bulk_create(systems)
    base_planets = BasePlanet.objects.filter(base_system_id__in=[system.base_id for system in systems])
    planets = [_init_planet(systems, base_planet) for base_planet in base_planets]
    Planet.objects.bulk_create(planets)


def _init_planet(systems: List[System], base_planet: BasePlanet) -> Planet:
    system = [system for system in systems if system.base_id == base_planet.base_system_id][0]
    player = None
    if system.base.faction is not None:
        player = Player.objects.get(game=system.game, faction=system.base.faction)
    return Planet(base=base_planet, system=system, owned_by=player)
