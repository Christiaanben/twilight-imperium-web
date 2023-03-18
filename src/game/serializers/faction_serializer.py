from rest_framework import serializers

from game.models import Faction


class FactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faction
        fields = ['id', 'name']
