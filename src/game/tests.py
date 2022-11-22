from django.test import TestCase

from game.models import Lobby


class ViewTests(TestCase):

    def test_lobby_create(self):
        # Setup
        data = {
            'name': 'lobby-name'
        }
        n_lobbies = Lobby.objects.count()
        # Execute
        response = self.client.post('/api/lobbies/', data=data)
        # Assert
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Lobby.objects.count(), n_lobbies + 1)
