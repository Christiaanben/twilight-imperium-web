"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
asgi_app = get_asgi_application()

import game.routing
from app.utils.middleware import TokenAuthMiddleware

application = ProtocolTypeRouter({
    "http": asgi_app,
    'websocket': TokenAuthMiddleware(
        AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(game.routing.websocket_urlpatterns))
        ))
})
