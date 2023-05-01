from django.utils import timezone
from app.settings import logger
from game.helpers import board_helper
from game.models.enums import UnitCategory
from game.models import Game, Strategy, BaseStrategy, BaseUnit, Unit, System, BaseCard, Card


def start_game(game: Game):
    logger.info(f'Starting a new game for {game}')
    game.started_at = timezone.now()
    game.speaker = game.players.order_by('?').first()
    game.save()
    board_helper.generate_board(game)
    _create_strategies(game)
    _init_players_tokens(game)
    _create_units(game)
    _create_starting_objectives(game)


def _create_strategies(game: Game):
    strategies = [Strategy(game=game, base=base) for base in BaseStrategy.objects.all()]
    Strategy.objects.bulk_create(strategies)


def _init_players_tokens(game: Game):
    logger.info(f'Initializing players tokens for {game.id}')
    game.players.update(
        n_tactic_tokens=3,
        n_fleet_tokens=3,
        n_strategy_tokens=2,
    )

def _create_units(game: Game):
    """
    Create the units for each player
    :param game: Game
    :return:
    """
    for player in game.players.all():
        home_system = System.objects.get(base__faction=player.faction, game=game)
        main_planet = home_system.planets.order_by('-base__resource').first()
        units = []
        for unit_type in player.faction.starting_units:
            base = BaseUnit.objects.get(type=unit_type)
            planet = main_planet if UnitCategory.is_allowed_on_planets(base.category) else None
            units.append(Unit(base=base, owned_by=player, system=home_system, planet=planet))
        Unit.objects.bulk_create(units)


def _create_starting_objectives(game: Game):
    """
    Create first 2 starting objectives.
    :param game: Game
    :return:
    """
    picked_objectives = []
    for base_objective in BaseCard.objects.filter(type='stage_1').order_by("?")[:2]:
        picked_objectives.append(Card(base=base_objective, game=game))
    Card.objects.bulk_create(picked_objectives)

