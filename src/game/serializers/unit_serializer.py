from rest_framework import serializers

from game.models import Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['system', 'owned_by', 'type', 'planet']

    system = serializers.IntegerField(source='system.base_id')
    planet = serializers.CharField(source='planet.base_id', allow_null=True)
    type = serializers.CharField(source='base.type')
