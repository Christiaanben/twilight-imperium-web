from rest_framework import serializers

from game.models import Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['system', 'owned_by', 'type']

    system = serializers.IntegerField(source='system.base_id')
    type = serializers.CharField(source='base.type')
