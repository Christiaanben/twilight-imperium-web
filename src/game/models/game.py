from django.db import models
from shortuuid import django_fields


class Game(models.Model):
    # Primary key
    id = django_fields.ShortUUIDField(length=8, primary_key=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        default_related_name = 'games'
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
