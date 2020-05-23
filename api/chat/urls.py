from django.urls import path

from chat.views import get_chatter_user, get_chatters

urlpatterns = [
    path('chatUser', get_chatter_user, name='get_chatter_user'),
    path('chatUsers', get_chatters, name='get_chat_users'),
]
