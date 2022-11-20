from rest_framework import routers

import game.viewsets

router = routers.DefaultRouter()
router.register(r'lobbies', viewset=game.viewsets.LobbyViewSet)
