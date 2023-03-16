from django.core.exceptions import ValidationError
from django.db import models

from game.models.enums import UnitType


def validate_unit_types(value):
    for unit_type in value:
        if unit_type not in UnitType.values:
            raise ValidationError(
                f'{unit_type} is not a valid unit type. Valid unit types are: {UnitType.values}'
            )


class Faction(models.Model):
    # Primary key
    id = models.SlugField(max_length=30, primary_key=True)
    # Fields
    name = models.CharField(max_length=40)
    starting_units = models.JSONField(blank=True, default=list, validators=[validate_unit_types])

    class Meta:
        default_related_name = 'factions'
        verbose_name = 'Faction'
        verbose_name_plural = 'Factions'

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Faction(id={self.id})'

