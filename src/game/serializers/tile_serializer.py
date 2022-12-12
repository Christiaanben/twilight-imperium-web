from rest_framework import serializers

from game.models import Tile
from .planet_serializer import PlanetSerializer


class TileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = ['id', 'q', 'r', 'planets']

    id = serializers.IntegerField(source='base.id')
    planets = PlanetSerializer(many=True)
