from app.utils.tests import DBTestCase
from game.helpers import game_manager
from game.models import Game


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
