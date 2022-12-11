from django.db import models


class Game(models.Model):
    pass

    class Meta:
        default_related_name = 'games'
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
