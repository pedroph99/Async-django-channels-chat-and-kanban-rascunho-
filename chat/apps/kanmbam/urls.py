from django.contrib import admin
from django.urls import path
from . import views as v
from django.contrib.auth.decorators import login_required

app_name = 'kanmbam_app'


urlpatterns = [
    path('home/', v.kanmbam_home, name='home')
]
