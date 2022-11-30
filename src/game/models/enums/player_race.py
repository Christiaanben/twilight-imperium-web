from django.db import models


class PlayerRace(models.TextChoices):
    XXCHA = 'xxcha'
    LETNEV = 'letnev'
    SOL = 'sol'
    NORR = 'norr'
    HACAN = 'hacan'
    JOL_NAR = 'jol-nar'
