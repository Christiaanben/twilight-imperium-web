from rest_framework import serializers

from game.models import Player


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['color', 'user', 'race']
