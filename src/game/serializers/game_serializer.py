from rest_framework import serializers

from game.models import Game
from .strategy_serializer import StrategySerializer
from .system_serializer import SystemSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['systems', 'phase', 'strategies']

    systems = SystemSerializer(many=True)
    strategies = StrategySerializer(many=True)
