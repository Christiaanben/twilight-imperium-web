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
            events = await lobby_helper.handle_new_or_returning_player(self.user.id, self.lobby_id)
            for event in events:
                await self.channel_layer.group_send(self.lobby_channel, event)
        else:
            await self.close(code=status.HTTP_401_UNAUTHORIZED)

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.lobby_channel, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if data['type'] == 'update_player':
            events = await lobby_helper.handle_update_player(self.user.id, data['kwargs']['player'])
            for event in events:
                await self.channel_layer.group_send(
                    self.lobby_channel, event
                )
        else:
            await self.channel_layer.group_send(self.lobby_channel, data)

    async def new_player(self, data):
        await self.send(text_data=json.dumps(data))

    async def update_player(self, data):
        await self.send(text_data=json.dumps(data))

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({'message': message}))
