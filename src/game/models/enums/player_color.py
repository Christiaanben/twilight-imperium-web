from django.db import models


class PlayerColor(models.TextChoices):
    RED = 'red'
    GREEN = 'green'
    YELLOW = 'yellow'
    PURPLE = 'purple'
    BLACK = 'black'
    BLUE = 'blue'
