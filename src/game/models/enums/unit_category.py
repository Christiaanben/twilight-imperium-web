from django.db import models


class UnitCategory(models.TextChoices):
    GROUND_FORCE = 'ground_force'
    SHIP = 'ship'
    STRUCTURE = 'structure'

    @classmethod
    def is_allowed_on_planets(cls, category: str) -> bool:
        return category in [cls.GROUND_FORCE, cls.STRUCTURE]
