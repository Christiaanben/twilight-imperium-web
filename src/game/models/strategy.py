from django.db import models

from .enums import StrategyType


class Strategy(models.Model):
    # Foreign keys
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE)
    player = models.ForeignKey('game.Player', on_delete=models.SET_NULL, null=True)
    # Fields
    type = models.PositiveSmallIntegerField(choices=StrategyType.choices)
    n_trade_goods = models.PositiveSmallIntegerField(default=0)

    class Meta:
        default_related_name = 'strategies'
        verbose_name = 'Strategy'
        verbose_name_plural = 'Strategies'
        unique_together = [('game', 'type')]
