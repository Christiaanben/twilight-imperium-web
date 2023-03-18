from django.db import models


class BaseSystem(models.Model):
    # Primary key
    id = models.PositiveSmallIntegerField(primary_key=True)
    # Foreign keys
    faction = models.ForeignKey('game.Faction', on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        default_related_name = 'base_systems'
        verbose_name = 'Base System'
        verbose_name_plural = 'Base Systems'

    def __repr__(self):
        return f'BaseSystem(id={self.id}, faction={self.faction_id})'

    def __str__(self):
        return f'{self.id}'
