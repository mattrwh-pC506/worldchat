from django.urls import path

from authentication.views import login, register, ping, username_available

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('ping', ping, name='ping'),
    path('usernameAvailable/<username>', username_available, name='username_available'),
]
