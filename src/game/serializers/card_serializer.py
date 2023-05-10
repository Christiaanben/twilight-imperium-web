from rest_framework import serializers
from game.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('name', 'type', 'subtitle', 'body', 'flavor', 'victory_points', 'owned_by')

    name = serializers.CharField(source='base.name')
    type = serializers.CharField(source='base.type')
    subtitle = serializers.CharField(source='base.subtitle')
    body = serializers.CharField(source='base.body')
    flavor = serializers.CharField(source='base.flavor')
    victory_points = serializers.IntegerField(source='base.victory_points')
