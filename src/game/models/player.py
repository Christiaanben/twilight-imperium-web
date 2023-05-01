from django.db import models

from .enums import Faction, PlayerColor


class Player(models.Model):
    # Foreign keys
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='players')
    faction = models.ForeignKey('game.Faction', on_delete=models.SET_NULL, null=True, default=None)
    # Timestamps
    created_at = models.DateTimeField(auto_now=True)
    # Fields
    color = models.CharField(choices=PlayerColor.choices,
                             max_length=max([len(v) for v in PlayerColor.values]),
                             default=None, null=True, blank=False)
    is_ready = models.BooleanField(default=False)
    n_tactic_tokens = models.IntegerField(default=0)
    n_fleet_tokens = models.IntegerField(default=0)
    n_strategy_tokens = models.IntegerField(default=0)
    n_trade_goods = models.IntegerField(default=0)
    n_commodities = models.IntegerField(default=0)

    class Meta:
        default_related_name = 'players'
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        unique_together = [('user', 'game'), ('game', 'faction'), ('game', 'color')]

    def __repr__(self):
        return f'Player(id={self.id}, faction={self.faction_id} user_id={self.user_id}, game_id={self.game_id})'

    def __str__(self):
        return repr(self)

    @property
    def n_victory_points(self) -> int:
        return 0
