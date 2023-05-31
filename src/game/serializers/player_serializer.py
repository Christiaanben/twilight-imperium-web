from rest_framework import serializers

from game.models import Player
from user.serializers import UserSerializer


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = [
            'id',
            'color',
            'user',
            'faction',
            'is_ready',
            'n_tactic_tokens',
            'n_fleet_tokens',
            'n_strategy_tokens',
            'n_trade_goods',
        ]

    user = UserSerializer(read_only=True)
