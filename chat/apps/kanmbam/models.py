from enum import unique
from django.db import models
from django.contrib.auth.models import User
import random
from django.urls import reverse

class tarefa(models.Model):
    TIPO = [
        ('AF', 'A fazer'),
        ('FE', 'FEITA'),
    ]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=TIPO)
    data_criacao = models.DateTimeField(auto_now_add=True)
    