from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('locations/', include('locations.urls')),
    path('chat/', include('chat.urls')),
]
