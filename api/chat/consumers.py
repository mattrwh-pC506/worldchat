from typing import Dict, Coroutine
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from common.types.typedtuple import typed_tuple_to_dict
from chat.types.message import MessageEvent
from chat.models import Chatter 

@sync_to_async
def get_chatter(username: str) -> Chatter:
    return Chatter.objects.get(user__username=username)

@sync_to_async
def save_chatter(chatter: Chatter):
    chatter.save()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> Coroutine:
        self.conversation = self.scope['url_route']['kwargs']['conversation']
        await self.channel_layer.group_add(self.conversation, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code: int) -> Coroutine:
        await self.channel_layer.group_discard(self.conversation, self.channel_name)

    async def receive(self, text_data: str) -> Coroutine:
        message = json.loads(text_data)
        await self.channel_layer.group_send(
                self.conversation, message)

    async def CHATTER_JOINED(self, message: Dict) -> Coroutine:
        chatter_username = message.get("chatter", {}).get("username", "")
        chatter = await get_chatter(chatter_username)
        chatter.online = True
        await save_chatter(chatter)
        await self.send(text_data=json.dumps(message))

    async def CHATTER_LEFT(self, message: Dict) -> Coroutine:
        chatter_username = message.get("chatter", {}).get("username", "")
        chatter = await get_chatter(chatter_username)
        chatter.online = False
        await save_chatter(chatter)
        await self.send(text_data=json.dumps(message))

    async def SET_NEW_MESSAGE(self, message: Dict) -> Coroutine:
        await self.send(text_data=json.dumps(message))
