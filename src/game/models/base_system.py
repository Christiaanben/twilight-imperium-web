from django.db import models

from game.models.enums import Faction


class BaseSystem(models.Model):
    # Primary key
    id = models.PositiveSmallIntegerField(primary_key=True)
    # Fields
    faction = models.CharField(choices=Faction.choices,
                               max_length=max([len(v) for v in Faction.values]),
                               default=None, null=True, blank=True)

    class Meta:
        default_related_name = 'base_systems'
        verbose_name = 'Base System'
        verbose_name_plural = 'Base Systems'

    def __str__(self):
        return f'{self.id}'
