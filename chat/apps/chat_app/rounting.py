from django.urls import re_path, path

from . import consumers as c
websocket_urlpatterns = [
    path('ws/home/<slug:slug>/', c.ChatConsumer.as_asgi())
]
