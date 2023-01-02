from rest_framework import routers

import game.viewsets
import users.viewsets

router = routers.DefaultRouter()
router.register(r'lobbies', viewset=game.viewsets.LobbyViewSet)
router.register(r'users', viewset=users.viewsets.UserViewSet)
router.register(r'games', viewset=game.viewsets.GameViewSet)