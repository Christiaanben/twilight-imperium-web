from django.db import models


class TechnologyType(models.TextChoices):
    BIOTIC = 'biotic'
    WARFARE = 'warfare'
    PROPULSION = 'propulsion'
    CYBERNETIC = 'cybernetic'
