from django.db import models


class UnitType(models.TextChoices):
    FLAGSHIP = 'flagship'
    WAR_SUN = 'war_sun'
    DREADNOUGHT = 'dreadnought'
    CARRIER = 'carrier'
    CRUISER = 'cruiser'
    DESTROYER = 'destroyer'
    FIGHTER = 'fighter'
    INFANTRY = 'infantry'
    PDS = 'pds'
    SPACE_DOCK = 'space_dock'
