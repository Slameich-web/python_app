from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group
from django.db import models


class User(models.Model):
    telegram_ID = models.CharField(max_length=16)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    middlename = models.CharField(max_length=64)
    city = models.ForeignKey(to='city.City', on_delete=models.SET_NULL, null=True, verbose_name='Город')
    role = models.CharField(max_length=64)

    def __str__(self):
        return self.firstname

class Product(models.Model):
    title = models.CharField(max_length=128)
    cost = models.IntegerField()
    
    def __str__(self):
        return self.title

class UserIncome(models.Model):
    date = models.DateField(max_length=64)
    sum = models.IntegerField()
    user = models.CharField(max_length=64)
    product = models.CharField(max_length=64)
    quantityProductSold = models.IntegerField()
    
    def __str__(self):
        return f"{self.date} {self.user} {self.sum}"

class Mailing(models.Model):
    text = models.CharField(max_length=128)
    files = models.FileField(max_length=64)
    date = models.DateTimeField(max_length=64)
    
    def __str__(self):
        return f"{self.text} {self.date}"
