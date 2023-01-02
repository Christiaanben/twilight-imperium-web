from rest_framework import serializers

from game.models import Player
from users.serializers import UserSerializer


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['id', 'color', 'user', 'faction', 'is_ready']

    user = UserSerializer(read_only=True)
