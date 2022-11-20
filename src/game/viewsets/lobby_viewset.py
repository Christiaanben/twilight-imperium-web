from rest_framework import viewsets

from game.models import Lobby
from game.serializers import LobbySerializer


class LobbyViewSet(viewsets.ModelViewSet):
    queryset = Lobby.objects.all()
    serializer_class = LobbySerializer
