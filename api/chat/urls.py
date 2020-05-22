from django.urls import path

from chat.views import index, room, login, register, get_chatter_user, get_chatters, ping

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('ping', ping, name='ping'),
    path('chatUser', get_chatter_user, name='get_chatter_user'),
    path('chatUsers', get_chatters, name='get_chat_users'),
]
