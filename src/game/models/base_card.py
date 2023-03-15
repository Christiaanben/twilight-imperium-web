from django.db import models
from game.models.enums.card_type import CardType


class BaseCard(models.Model):
    id = models.SlugField(max_length=30, primary_key=True)
    name = models.SlugField(max_length=30)
    type = models.CharField(choices=CardType.choices,
                            max_length=max([len(card_name) for card_name in CardType.values]),
                            default=None, null=False, blank=False)
    victory_points = models.PositiveSmallIntegerField(default=0)

    class Meta:
        default_related_name = 'base_cards'
        verbose_name = 'BaseCard'
        verbose_name_plural = 'BaseCards'

    def __repr__(self):
        return f'BaseCard(id={self.id}, type={self.type}, VP={self.victory_points})'

    def __str__(self):
        return self.name
