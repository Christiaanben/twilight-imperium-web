from django.db import models

from .enums import UnitType, Faction


class BaseUnit(models.Model):
    # Primary key
    id = models.SlugField(primary_key=True, max_length=30)
    # Foreign keys
    faction = models.ForeignKey('game.Faction', on_delete=models.SET_NULL, null=True, default=None)
    # Fields
    name = models.CharField(max_length=30, blank=False)
    movement = models.PositiveSmallIntegerField(default=0)
    cost = models.PositiveSmallIntegerField(default=0)
    combat = models.PositiveSmallIntegerField(default=0)
    capacity = models.PositiveSmallIntegerField(default=0)
    type = models.SlugField(choices=UnitType.choices, max_length=max([len(val) for val in UnitType.values]))

    class Meta:
        default_related_name = 'base_units'
        verbose_name = 'Base Unit'
        verbose_name_plural = 'Base Units'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'BaseUnit(id={self.id}, type={self.type})'
