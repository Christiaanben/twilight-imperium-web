from rest_framework import serializers

from game.models import Game
from .player_serializer import PlayerSerializer


class LobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'players']

    players = PlayerSerializer(many=True, read_only=True)
