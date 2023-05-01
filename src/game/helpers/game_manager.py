from django.utils import timezone
from app.settings import logger
from game.models import Game, Strategy, BaseStrategy, BaseUnit, Unit, System, BaseCard, Card


def start_game(game_id: str):
    logger.info(f'Starting a new game for {game_id}')
    game = Game.objects.get(id=game_id)
    game.started_at = timezone.now()
    game.speaker = game.players.order_by('?').first()
    game.save()
    _create_strategies(game)
    _create_units(game)
    _create_starting_objectives(game)
    # board_helper.generate_board(game)
    # GameConsumer.create_new_game(game_id)


def _create_strategies(game: Game):
    strategies = [Strategy(game=game, base=base) for base in BaseStrategy.objects.all()]
    Strategy.objects.bulk_create(strategies)


def _create_units(game: Game):
    """
    Create the units for each player
    :param game: Game
    :return:
    """
    for player in game.players.all():
        home_system = System.objects.get(base__faction=player.faction, game=game)
        units = []
        for unit_type in player.faction.starting_units:
            base = BaseUnit.objects.get(type=unit_type)
            units.append(Unit(base=base, owned_by=player, system=home_system))
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

