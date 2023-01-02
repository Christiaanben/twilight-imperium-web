from django.db import models

from .enums import PlayerRace, PlayerColor


class Player(models.Model):
    # Foreign keys
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    lobby = models.ForeignKey('game.Lobby', on_delete=models.CASCADE)
    # Timestamps
    created_at = models.DateTimeField(auto_now=True)
    # Fields
    race = models.CharField(choices=PlayerRace.choices,
                            max_length=max([len(v) for v in PlayerRace.values]),
                            default=None, null=True, blank=False)
    color = models.CharField(choices=PlayerColor.choices,
                             max_length=max([len(v) for v in PlayerColor.values]),
                             default=None, null=True, blank=False)

    class Meta:
        default_related_name = 'players'
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        unique_together = [('user', 'lobby'), ('lobby', 'race'), ('lobby', 'color')]

    def __str__(self):
        return f'{self.user} on {self.lobby_id}'

