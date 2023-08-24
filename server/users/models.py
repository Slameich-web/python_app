from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group
from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=64, verbose_name='E-mail', unique=True)
    telegram_id = models.CharField(max_length=32, verbose_name='ID Telegram', unique=True)
    first_name = models.CharField(max_length=32, verbose_name='Имя')
    middle_name = models.CharField(max_length=32, verbose_name='Отчество', blank=True, null=True)
    last_name = models.CharField(max_length=32, verbose_name='Фамилия')

    city = models.ForeignKey(to='city.City', on_delete=models.SET_NULL, null=True, verbose_name='Город')

    role = models.ForeignKey(to=Group, on_delete=models.SET_NULL, null=True, verbose_name='Роль', related_name='users')

    def __str__(self):
        return f'{self.pk}. Пользователь {self.last_name} {self.first_name[0]}. {self.middle_name[0]}.'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'