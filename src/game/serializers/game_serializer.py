from rest_framework import serializers

from game.models import Game
from .player_serializer import PlayerSerializer
from .strategy_serializer import StrategySerializer
from .system_serializer import SystemSerializer
from .card_serializer import CardSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['systems', 'phase', 'strategies', 'players']

    systems = SystemSerializer(many=True)
    strategies = StrategySerializer(many=True)
    players = PlayerSerializer(many=True)
    cards = CardSerializer(many=True)
