from django.test import TestCase
from rest_framework.reverse import reverse

from app.utils.tests import DBTestCase
from game.models import Game


class LobbyViewTests(TestCase):

    def test_lobby_create(self):
        # Setup
        data = {
            'name': 'lobby-name'
        }
        n_lobbies = Game.objects.count()
        # Execute
        response = self.client.post('/api/lobbies/', data=data)
        # Assert
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Game.objects.count(), n_lobbies + 1)


class GameViewTests(DBTestCase):

    fixtures = DBTestCase.fixtures + ['game/fixtures/tests/new_game.yaml']

    def test_get_game(self):
        # Execute
        response = self.client.get(reverse('game-detail', kwargs={'pk': 'new_game'}))
        # Assert
        self.assertEquals(response.status_code, 200)
