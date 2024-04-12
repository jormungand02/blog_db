from typing import Any
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор', blank=True)

    title = models.CharField(max_length=100, verbose_name='Название')

    image = models.ImageField(upload_to='posts_img/', blank=True, verbose_name='Фото')

    description = models.TextField(blank=True, verbose_name='Описание')

    created_at = models.DateTimeField(auto_now_add=True)