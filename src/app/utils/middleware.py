from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token


@database_sync_to_async
def fetch_user(token: str):
    try:
        return Token.objects.get(key=token).user
    except Token.DoesNotExist:
        return AnonymousUser()


class TokenAuthMiddleware:
    """
    TokenAuthMiddleware does token authentication on the websocket.
    Specifically it looks for the token in the query params
    """

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        query_params = parse_qs(scope["query_string"].decode())
        token = query_params['token'][0]
        scope["user"] = await fetch_user(token)
        return await self.app(scope, receive, send)


