from django.db import models


class Planet(models.Model):
    # Foreign keys
    tile = models.ForeignKey('game.Tile', on_delete=models.CASCADE)
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
