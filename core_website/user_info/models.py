from django.contrib.auth.models import User
from django.db import models

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info', verbose_name='Информация о пользователе')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    tel = models.CharField(max_length=10, blank=True, verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='Почта')
