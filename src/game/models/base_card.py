from django.db import models

from .enums import CardType, CardTrigger


class BaseCard(models.Model):
    id = models.SlugField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    type = models.SlugField(choices=CardType.choices,
                            max_length=max([len(card_name) for card_name in CardType.values]), null=False, blank=False)
    trigger = models.SlugField(choices=CardTrigger.choices,
        max_length=max([len(trigger) for trigger in CardTrigger.values]), null=True, blank=True)
    subtitle = models.CharField(max_length=30, blank=True, default='')
    body = models.CharField(max_length=200, blank=True, default='')
    flavor = models.CharField(max_length=200, blank=True, default='')
    victory_points = models.PositiveSmallIntegerField(default=0)

    class Meta:
        default_related_name = 'base_cards'
        verbose_name = 'BaseCard'
        verbose_name_plural = 'BaseCards'

    def __repr__(self):
        return f'BaseCard(id={self.id}, type={self.type}, VP={self.victory_points})'

    def __str__(self):
        return self.name
