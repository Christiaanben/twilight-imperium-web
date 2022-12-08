from rest_framework import serializers

from game.models import Player
from user.serializers import UserSerializer


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['id', 'color', 'user', 'race']

    user = UserSerializer(read_only=True)
