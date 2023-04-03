from rest_framework import serializers

from game.models import System
from .planet_serializer import PlanetSerializer


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ['id', 'q', 'r', 'planets', 'activated_by']

    id = serializers.IntegerField(source='base.id')
    planets = PlanetSerializer(many=True)
