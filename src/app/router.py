from rest_framework import routers

import game.viewsets
import user.viewsets

router = routers.DefaultRouter()
router.register(r'lobbies', viewset=game.viewsets.LobbyViewSet)
router.register(r'users', viewset=user.viewsets.UserViewSet)
