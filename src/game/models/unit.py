from django.db import models


class Unit(models.Model):
    # Foreign keys
    owned_by = models.ForeignKey('game.Player', on_delete=models.CASCADE)
    base = models.ForeignKey('game.BaseUnit', on_delete=models.CASCADE)
    system = models.ForeignKey('game.System', on_delete=models.CASCADE)
    planet = models.ForeignKey('game.Planet', on_delete=models.SET_NULL, null=True, default=None)
    # Fields
    is_damaged = models.BooleanField(default=False)

    class Meta:
        default_related_name = 'units'
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

    def __str__(self):
        return f'{self.base_id}'

    def __repr__(self):
        return f'Unit(id={self.id}, base_id={self.base_id}, owned_by={self.owned_by_id}, system={self.system_id}, ' \
               f'planet={self.planet_id})'
