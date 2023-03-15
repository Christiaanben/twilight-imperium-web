from django.db import models


class Card(models.Model):
    # ForeignKeys
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE)
    base = models.ForeignKey('game.BaseCard', on_delete=models.CASCADE)
    claimed_by = models.ManyToManyField('game.Player', related_name='claimed_cards')
    owned_by = models.ForeignKey('game.Player', null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'cards'
        verbose_name_plural = 'Cards'

    def __repr__(self):
        return f'Card(id={self.id}, base id={self.base_id})'

    def __str__(self):
        return self.base.name
