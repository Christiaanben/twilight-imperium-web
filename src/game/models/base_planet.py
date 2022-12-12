from django.db import models

from game.models.enums import PlanetTrait, TechnologyType


class BasePlanet(models.Model):
    id = models.SlugField(max_length=30, primary_key=True)
    # Foreign keys
    base_tile = models.ForeignKey('game.BaseTile', on_delete=models.CASCADE)
    # Fields
    name = models.CharField(max_length=30)
    resource = models.PositiveSmallIntegerField()
    influence = models.PositiveSmallIntegerField()
    trait = models.CharField(choices=PlanetTrait.choices,
                             max_length=max([len(v) for v in PlanetTrait.values]),
                             default=None, null=True, blank=False)
    technology = models.CharField(choices=TechnologyType.choices,
                                  max_length=max([len(v) for v in TechnologyType.values]),
                                  default=None, null=True, blank=False)

    class Meta:
        default_related_name = 'base_planets'
        verbose_name = 'BasePlanet'
        verbose_name_plural = 'BasePlanets'

    def __str__(self):
        return self.name
