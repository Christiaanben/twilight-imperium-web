from django.db import models


class System(models.Model):
    # Foreign keys
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE)
    base = models.ForeignKey('game.BaseSystem', on_delete=models.CASCADE)
    # Fields
    q = models.SmallIntegerField()
    r = models.SmallIntegerField()

    class Meta:
        default_related_name = 'systems'
        verbose_name = 'System'
        verbose_name_plural = 'Systems'
        unique_together = [('game', 'q', 'r'), ('game', 'base')]

    def __repr__(self):
        return f'{self.game_id}-{self.base_id}'
