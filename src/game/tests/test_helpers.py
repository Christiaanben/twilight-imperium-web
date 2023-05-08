from app.utils.tests import DBTestCase
from game.helpers import game_manager, board_helper
from game.models import Game, Planet


class GameManagerTests(DBTestCase):

    fixtures = DBTestCase.fixtures + ['game/fixtures/tests/new_game.yaml']

    def test_init_players_tokens(self):
        # Setup
        game = Game.objects.get(id='new_game')
        # Execute
        game_manager._init_players_tokens(game)
        # Assert
        players = game.players.all()
        self.assertGreaterEqual(len(players), 2)
        for player in players:
            self.assertEquals(player.n_tactic_tokens, 3)
            self.assertEquals(player.n_fleet_tokens, 3)
            self.assertEquals(player.n_strategy_tokens, 2)


class BoardHelperTests(DBTestCase):

    fixtures = DBTestCase.fixtures + ['game/fixtures/tests/new_game.yaml']

    def test_init_planet_owned_by(self):
        # Setup
        game = Game.objects.get(id='new_game')
        # Execute
        board_helper.generate_board(game)
        # Assert
        self.assertEquals(Planet.objects.filter(owned_by__faction__id='sol').count(), 1)
        self.assertEquals(Planet.objects.filter(owned_by__faction__id='hacan').count(), 3)
        self.assertIsNone(Planet.objects.get(base_id='mecatol_rex').owned_by)
