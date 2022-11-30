from django.db import models

from .enums import PlayerRace, PlayerColor


class Player(models.Model):
    race = models.CharField(choices=PlayerRace.choices,
                            max_length=max([len(v) for v in PlayerRace.values]),
                            default=None, null=True, blank=False)
    color = models.CharField(choices=PlayerColor.choices,
                             max_length=max([len(v) for v in PlayerColor.values]),
                             default=None, null=True, blank=False)
