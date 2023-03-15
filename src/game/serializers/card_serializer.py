from rest_framework import serializers
from game.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('name', 'type', 'victory_points')

    name = serializers.CharField(source='base.name')
    type = serializers.CharField(source='base.type')
    victory_points = serializers.IntegerField(source='base.victory_points')
