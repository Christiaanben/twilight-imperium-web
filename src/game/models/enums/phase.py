from django.db import models


class Phase(models.TextChoices):
    STRATEGY = 'strategy'
    ACTION = 'action'
    STATUS = 'status'
    AGENDA = 'agenda'
