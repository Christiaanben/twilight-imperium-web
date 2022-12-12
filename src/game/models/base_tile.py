from django.db import models

from game.models.enums import Faction


class BaseTile(models.Model):
    # Primary key
    id = models.PositiveSmallIntegerField(primary_key=True)
    # Fields
    faction = models.CharField(choices=Faction.choices,
                               max_length=max([len(v) for v in Faction.values]),
                               default=None, null=True, blank=False)

    class Meta:
        default_related_name = 'base_tiles'
        verbose_name = 'BaseTile'
        verbose_name_plural = 'BaseTiles'

    def __str__(self):
        return f'{self.id}'
