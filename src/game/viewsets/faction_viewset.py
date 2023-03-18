from rest_framework import viewsets

from game.models import Faction
from game.serializers import FactionSerializer


class FactionViewSet(viewsets.ModelViewSet):
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer
