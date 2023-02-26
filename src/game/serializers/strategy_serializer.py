from rest_framework import serializers

from game.models import Strategy


class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ('type',)
