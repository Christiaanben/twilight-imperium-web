import json

from channels.db import database_sync_to_async as db_async
from channels.generic.websocket import AsyncWebsocketConsumer

from app.settings import logger
from game.helpers.commands import COMMANDS
from game.models import Player, Game


class GameConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.game = None
        self.game_channel = None
        self.player = None
        self.game_id = None

    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_channel = f'game_{self.game_id}'
        self.game = await db_async(Game.objects.get)(id=self.game_id)
        self.player = await db_async(Player.objects.get)(user=self.scope['user'], game_id=self.game_id)

        await self.channel_layer.group_add(self.game_channel, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        logger.info(f"Received data: {data}")
        
        command_class = COMMANDS.get(data['type'])
        command = command_class(**data['kwargs'])
        events = await db_async(command.execute)(self.game, self.player)
        for event in events:
            await self.channel_layer.group_send(
                self.game_channel,
                {
                    'type': 'broadcast',
                    'event': event
                }
            )

    async def broadcast(self, data):
        await self.send(text_data=json.dumps(data.get('event')))
