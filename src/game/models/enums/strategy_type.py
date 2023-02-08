from django.db import models


class StrategyType(models.IntegerChoices):
    LEADERSHIP = 1
    DIPLOMACY = 2
    POLITICS = 3
    CONSTRUCTION = 4
    TRADE = 5
    WARFARE = 6
    TECHNOLOGY = 7
    IMPERIAL = 8
