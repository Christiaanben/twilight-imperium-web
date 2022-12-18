from django.db import models


class Faction(models.TextChoices):
    XXCHA = 'xxcha'
    SOL = 'sol'
    HACAN = 'hacan'
    LETNEV = 'letnev'
    SARDAKK_NORR = 'sardakk_norr'
    JOL_NAR = 'jol_nar'
