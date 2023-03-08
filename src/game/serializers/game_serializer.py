from rest_framework import serializers

from game.models import Game
from . import PlayerSerializer
from .strategy_serializer import StrategySerializer
from .system_serializer import SystemSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['systems', 'phase', 'strategies', 'players']

    systems = SystemSerializer(many=True)
    strategies = StrategySerializer(many=True)
    players = PlayerSerializer(many=True)
