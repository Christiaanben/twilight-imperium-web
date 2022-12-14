from django.core.validators import MinLengthValidator
from django.db import models
from shortuuid import django_fields


class Game(models.Model):
    # Primary key
    id = django_fields.ShortUUIDField(length=8, primary_key=True)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Fields
    name = models.CharField(max_length=30, blank=False, default='', validators=[MinLengthValidator(3)])

    class Meta:
        default_related_name = 'games'
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __repr__(self):
        return f'Game(id={self.id})'

    def __str__(self):
        return f'{self.id} - "{self.name}"'
