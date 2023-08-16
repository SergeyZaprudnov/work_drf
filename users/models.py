from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(max_length=100, verbose_name='Электронная почта', unique=True)
    city = models.CharField(max_length=150, verbose_name='Город')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    avatar = models.ImageField(upload_to='avatar.png', verbose_name='Аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'
