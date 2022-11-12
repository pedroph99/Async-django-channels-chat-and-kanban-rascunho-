from enum import unique
from django.db import models
from django.contrib.auth.models import User
import random
from django.urls import reverse
# Create your models here.
class usuarios(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, unique=True, blank=True)
   
    def get_slug():
        slug = ''
        slug = str(random.randint(11111111, 99999999))

        return slug

    def get_absolute_url(self):
        return reverse("chat_app:initial", kwargs={"slug": self.slug})  # new
    
    def save(self, *args, **kwargs):
        try:
            self.slug = ''.join(str(random.randint(0, 9)) for _ in range(8))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)
        

class Todo(models.Model):
    user = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    mensagem = models.TextField()
    ativo = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return reverse("chat_app:muda", kwargs={"pk": self.pk})  # new

class TodoManager(models.Manager):
    pass