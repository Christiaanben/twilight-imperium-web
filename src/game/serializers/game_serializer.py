from rest_framework import serializers

from game.models import Game
from .tile_serializer import TileSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['tiles']

    tiles = TileSerializer(many=True)
