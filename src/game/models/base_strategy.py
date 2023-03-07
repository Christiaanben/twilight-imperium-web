from django.db import models


class BaseStrategy(models.Model):
    # Primary key
    id = models.SlugField(primary_key=True)
    # Fields
    initiative = models.PositiveSmallIntegerField(default=0)
    label = models.CharField(max_length=50)

    class Meta:
        default_related_name = 'base_strategies'
