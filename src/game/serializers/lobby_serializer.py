from rest_framework import serializers

from game.models import Lobby


class LobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lobby
        fields = ['id', 'name']
