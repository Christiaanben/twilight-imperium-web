from rest_framework import serializers

from game.models import Game, Unit
from .strategy_serializer import StrategySerializer
from .system_serializer import SystemSerializer
from .unit_serializer import UnitSerializer
from .player_serializer import PlayerSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['systems', 'phase', 'strategies', 'players', 'units']

    systems = SystemSerializer(many=True)
    strategies = StrategySerializer(many=True)
    players = PlayerSerializer(many=True)
    units = serializers.SerializerMethodField()

    @staticmethod
    def get_units(game: Game):
        return UnitSerializer(Unit.objects.filter(owned_by__game=game), many=True).data
