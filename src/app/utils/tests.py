from django.test import TestCase


class DBTestCase(TestCase):
    fixtures = [
        # Seeds
        'game/fixtures/seeds/systems.yaml',
        'game/fixtures/seeds/planets.yaml',
        'game/fixtures/seeds/factions.yaml',
        'game/fixtures/seeds/units.yaml',
        # Tests
        'game/fixtures/tests/users.yaml',
    ]
