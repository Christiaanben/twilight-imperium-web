import json

from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework import status

from game.helpers import lobby_helper


class GameConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.lobby_id = None
        self.user = None
        self.lobby_channel = None

    async def connect(self):
        self.lobby_id = self.scope['url_route']['kwargs']['lobby_id']
        self.lobby_channel = f'lobby_{self.lobby_id}'
        self.user = self.scope['user']

        # Join room group
        await self.channel_layer.group_add(self.lobby_channel, self.channel_name)

        if self.user.is_authenticated:
            await self.accept()
            await self.channel_layer.group_send(
                self.lobby_channel, {'type': 'handle_new_or_returning_player', 'user': 'John'}
            )
        else:
            await self.close(code=status.HTTP_401_UNAUTHORIZED)

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.lobby_channel, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.lobby_channel, data
        )

    async def handle_new_or_returning_player(self, data):
        """
        If the user is new to the lobby, add them to the lobby (if there's space) and let everyone know.
        Else do nothing (or just update presence).
        """
        events = await lobby_helper.handle_new_or_returning_player(self.user, self.lobby_id)
        for event in events:
            await self.send(text_data=json.dumps(event))

    async def update_player(self, data):
        await self.send(text_data=json.dumps(data))

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({'message': message}))
