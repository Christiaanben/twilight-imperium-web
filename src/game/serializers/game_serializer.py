from rest_framework import serializers

from game.models import Game
from .system_serializer import SystemSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['systems', 'phase']

    systems = SystemSerializer(many=True)
