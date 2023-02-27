import json

from channels.db import database_sync_to_async as db_async
from channels.generic.websocket import AsyncWebsocketConsumer

from app.settings import logger
from game.helpers import status_phase_helper
from game.models import Player
from game.models.enums import StrategyType


class GameConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.player = None
        self.game_id = None

    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.player = await db_async(Player.objects.get)(user=self.scope['user'], game_id=self.game_id)
        await self.accept()

    async def disconnect(self, close_code):
        await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        logger.info(f"Received data: {data}")
        if data['type'] == 'select_strategy':
            strategy = await db_async(status_phase_helper.select_strategy)(
                player=self.player,
                strategy_type=getattr(StrategyType, data['kwargs']['strategy'].upper())
            )
            await self.send(text_data=json.dumps({
                'type': 'select_strategy',
                'kwargs': {
                    'type': strategy.type,
                }
            }))
