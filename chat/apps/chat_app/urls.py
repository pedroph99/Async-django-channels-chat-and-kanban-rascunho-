from django.contrib import admin
from django.urls import path
from . import views as v
from django.contrib.auth.decorators import login_required

app_name = 'chat_app'

urlpatterns = [
    path('', v.home, name='home'),
    path('home/<slug:slug>', login_required(v.home2.as_view()), name='initial'),
    path('home/todo/<int:pk>', v.Todo_Detail.as_view(), name='todo'),
    path('home/todo/muda_estado/<int:pk>', v.muda_estado, name='muda'),
    path('registro', v.register, name='registro')
]
