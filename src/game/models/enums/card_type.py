from django.db import models


class CardType(models.TextChoices):
    STAGE_1 = "stage_1"
    STAGE_2 = "stage_2"
    SECRET = "secret"
    ACTION = "action"
    AGENDA = "agenda"
    PROMISSORY = "promissory"

