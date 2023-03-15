from django.db import models


class Card(models.Model):
    # ForeignKeys
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='cards')
    base_id = models.ForeignKey('game.BaseCard', on_delete=models.CASCADE)
    claimed_by = models.ManyToManyField('game.Player', related_name='claims')
    owned_by = models.ForeignKey('game.Player', related_name='owned_by', on_delete=models.CASCADE)
