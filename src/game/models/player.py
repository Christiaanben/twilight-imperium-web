from django.db import models

from .enums import Faction, PlayerColor


class Player(models.Model):
    # Foreign keys
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='players')
    # Timestamps
    created_at = models.DateTimeField(auto_now=True)
    # Fields
    faction = models.CharField(choices=Faction.choices,
                               max_length=max([len(v) for v in Faction.values]),
                               default=None, null=True, blank=False)
    color = models.CharField(choices=PlayerColor.choices,
                             max_length=max([len(v) for v in PlayerColor.values]),
                             default=None, null=True, blank=False)
    is_ready = models.BooleanField(default=False)

    class Meta:
        default_related_name = 'players'
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        unique_together = [('user', 'game'), ('game', 'faction'), ('game', 'color')]

    def __repr__(self):
        return f'Player(id={self.id}, user_id={self.user_id}, lobby_id={self.game_id})'

    def __str__(self):
        return f'{self.user} on {self.game_id}'
