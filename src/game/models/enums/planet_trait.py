from django.db import models


class PlanetTrait(models.TextChoices):
    CULTURAL = 'cultural'
    HAZARDOUS = 'hazardous'
    INDUSTRIAL = 'industrial'
