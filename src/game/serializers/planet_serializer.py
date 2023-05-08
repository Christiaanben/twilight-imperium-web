from rest_framework import serializers

from game.models import Planet


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ['id', 'name', 'resource', 'influence', 'trait', 'technology', 'owned_by']

    id = serializers.CharField(source='base.id')
    name = serializers.CharField(source='base.name')
    resource = serializers.IntegerField(source='base.resource')
    influence = serializers.IntegerField(source='base.influence')
    trait = serializers.CharField(source='base.trait')
    technology = serializers.CharField(source='base.technology')
