from django.test import TestCase


class DBTestCase(TestCase):
    fixtures = [
        # Seeds
        'game/fixtures/seeds/systems.yaml',
        'game/fixtures/seeds/planets.yaml',
        # Tests
        'game/fixtures/tests/games.yaml',
    ]
