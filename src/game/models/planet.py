from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .system import System


class Planet(models.Model):
    # Foreign keys
    system = models.ForeignKey('game.System', on_delete=models.CASCADE)
    base = models.ForeignKey('game.BasePlanet', on_delete=models.CASCADE)
    # Fields
    is_exhausted = models.BooleanField(default=True)

    class Meta:
        default_related_name = 'planets'
        verbose_name = 'Planet'
        verbose_name_plural = 'Planets'
        unique_together = [('system', 'base')]

    def __str__(self):
        return f'{self.system_id}. {self.base_id}'
