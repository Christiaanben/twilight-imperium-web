from rest_framework import viewsets

from game.models import Game
from game.serializers import LobbySerializer


class LobbyViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = LobbySerializer
