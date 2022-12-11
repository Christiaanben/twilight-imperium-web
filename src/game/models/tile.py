from django.db import models


class Tile(models.Model):
    # Foreign keys
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE)
    base = models.ForeignKey('game.BaseTile', on_delete=models.CASCADE)
    # Fields
    q = models.SmallIntegerField()
    r = models.SmallIntegerField()

    class Meta:
        default_related_name = 'tiles'
        verbose_name = 'Tile'
        verbose_name_plural = 'Tiles'
        unique_together = [('game', 'q', 'r'), ('game', 'base')]
