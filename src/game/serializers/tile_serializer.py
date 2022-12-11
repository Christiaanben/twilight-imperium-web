from rest_framework import serializers

from game.models import Tile


class TileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = ['id', 'q', 'r']

    id = serializers.IntegerField(source='base.id')
