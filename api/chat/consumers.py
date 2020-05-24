from typing import Dict, Coroutine, Any
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User

from common.utils.distance import add_distance_to_chatter
from common.types.typedtuple import typed_tuple_to_dict
from chat.types.message import MessageEvent
from chat.models import Chatter 

@sync_to_async
def get_chatter(username: str) -> Chatter:
    return Chatter.objects.filter(user__username=username).first()

@sync_to_async
def get_user(username: str) -> Chatter:
    return User.objects.filter(username=username).first()

@sync_to_async
def get_chatters(user: User) -> Chatter:
    return [ add_distance_to_chatter(user)(chatter) for chatter in Chatter.objects.filter(online=True).all()]


@sync_to_async
def set_user_to_scope(user: User, consumer: Any) -> Chatter:
    if user: consumer.scope['user'] = user

@sync_to_async
def save_chatter(chatter: Chatter):
    chatter.save()

async def disconnect_chatter(username: str):
    chatter = await get_chatter(username)
    if chatter:
        chatter.online = False
        await save_chatter(chatter)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> Coroutine:
        self.conversation = self.scope['url_route']['kwargs']['conversation']
        await self.channel_layer.group_add(self.conversation, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code: int) -> Coroutine:
        user = self.scope.get("user")
        await disconnect_chatter(user.username)
        await self.channel_layer.group_discard(self.conversation, self.channel_name)

    async def receive(self, text_data: str) -> Coroutine:
        message = json.loads(text_data)
        await self.channel_layer.group_send(
                self.conversation, message)

    async def CHATTER_JOINED(self, message: Dict) -> Coroutine:
        chatter_username = message.get("chatter", {}).get("username", "")
        chatter = await get_chatter(chatter_username)
        chatter.online = True
        user = await get_user(chatter_username)
        await set_user_to_scope(user, self)
        await save_chatter(chatter)
        message = { **message, "chatters": await get_chatters(user) }
        await self.send(text_data=json.dumps(message))

    async def CHATTER_LEFT(self, message: Dict) -> Coroutine:
        chatter_username = message.get("chatter", {}).get("username", "")
        user = await get_user(chatter_username)
        message = { **message, "chatters": await get_chatters(user) }
        await disconnect_chatter(chatter_username)
        await self.send(text_data=json.dumps(message))

    async def SET_NEW_MESSAGE(self, message: Dict) -> Coroutine:
        await self.send(text_data=json.dumps(message))
