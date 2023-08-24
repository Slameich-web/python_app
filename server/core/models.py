from django.db import models
from django.urls import reverse

class User(models.Model):
    telegram_ID = models.CharField(max_length=16)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    middlename = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    role = models.CharField(max_length=64)

    def __str__(self):
        return self.firstname


class Platform(models.Model):
    title = models.CharField(max_length=128)
    
    def __str__(self):
        return self.title

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
