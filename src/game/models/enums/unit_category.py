from django.db import models


class UnitCategory(models.TextChoices):
    GROUND_FORCE = 'ground_force'
    SHIP = 'ship'
    STRUCTURE = 'structure'
