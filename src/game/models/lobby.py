from django.core.validators import MinLengthValidator
from django.db import models

from shortuuid import django_fields


class Lobby(models.Model):
    id = django_fields.ShortUUIDField(length=8, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=30, blank=False, default='', validators=[MinLengthValidator(3)])
