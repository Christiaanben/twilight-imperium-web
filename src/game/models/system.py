from django.db import models


class System(models.Model):
    # Foreign keys
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE)
    base = models.ForeignKey('game.BaseSystem', on_delete=models.CASCADE)
    activated_by = models.ManyToManyField('game.Player', related_name='activated_systems', blank=True)
    # Fields
    q = models.SmallIntegerField()
    r = models.SmallIntegerField()

    class Meta:
        default_related_name = 'systems'
        verbose_name = 'System'
        verbose_name_plural = 'Systems'
        unique_together = [('game', 'q', 'r'), ('game', 'base')]

    def __repr__(self):
        return f'System(id={self.id}, base={self.base_id}, game={self.game_id})'
    
    def __str__(self):
        return f'{self.game_id}-{self.base_id}'
