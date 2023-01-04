from django.db.models import Count

from app.utils.tests import DBTestCase
from game.models import Game, BaseSystem, System


# class ModelTests(DBTestCase):
#
#     def test_auto_create_planet(self):
#         # Setup
#         game = Game.objects.create(id='game0002')
#         base_system = BaseSystem.objects.annotate(n_planets=Count('base_planets')).filter(n_planets__gt=0).first()
#         # Execute
#         system = System.objects.create(game=game, base=base_system, q=0, r=0)
#         # Assert
#         self.assertGreater(system.planets.count(), 0, msg='Did not automatically create planets on system creation')
