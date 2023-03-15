from django.db import models


class CardType(models.TextChoices):
    OBJ_STAGE_1 = "stage_1"
    OBJ_STAGE_2 = "stage_2"
    OBJ_SECRET = "secret"
    ACTION = "action"
    AGENDA = "agenda"
    PROMISSORY = "promissory"

