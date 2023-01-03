from typing import List

from game.models import Game, System, BasePlanet, Planet

DEFAULT_BOARDS = {
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
    systems = [System(game=game, **system) for system in DEFAULT_BOARDS[3]]
    System.objects.bulk_create(systems)
    base_planets = BasePlanet.objects.filter(base_system_id__in=[system.base_id for system in systems])
    planets = [_init_planet(systems, base_planet) for base_planet in base_planets]
    Planet.objects.bulk_create(planets)


def _init_planet(systems: List[System], base_planet: BasePlanet) -> Planet:
    system = [system for system in systems if system.base_id == base_planet.base_system_id][0]
    return Planet(base=base_planet, system=system)
