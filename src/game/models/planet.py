from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .system import System


class Planet(models.Model):
    # Foreign keys
    tile = models.ForeignKey('game.System', on_delete=models.CASCADE)
    base = models.ForeignKey('game.BasePlanet', on_delete=models.CASCADE)
    # Fields
    is_exhausted = models.BooleanField(default=True)

    class Meta:
        default_related_name = 'planets'
        verbose_name = 'Planet'
        verbose_name_plural = 'Planets'
        unique_together = [('tile', 'base')]

    def __str__(self):
        return f'{self.tile_id}. {self.base_id}'


@receiver(post_save, sender=System)
def create_planets(instance: System, created: bool, **kwargs):
    if created:
        for base_planet in instance.base.base_planets.all():
            Planet.objects.create(tile=instance, base=base_planet)
