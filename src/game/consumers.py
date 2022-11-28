import json

from channels.generic.websocket import AsyncWebsocketConsumer


class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        lobby_id = self.scope['url_route']['kwargs']['lobby_id']
        self.room_group_name = 'chat_%s' % lobby_id

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        print('self.user', self.scope['user'])

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'handle_new_or_returning_player', 'user': 'John'}
        )

    async def handle_new_or_returning_player(self, data):
        """
        Checks if the user is signed in. Then, if they are already a part of the lobby do nothing (or update presence).
        Else add them to the lobby and let everyone in the lobby know of the new player
        """
        print('handling new or returning user', data)
        await self.send(text_data=json.dumps({'new_player': 'John'}))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'chat_message', 'message': message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({'message': message}))
