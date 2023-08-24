from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=256, verbose_name='Название')

    def __str__(self):
        return f'Продукт {self.name}'
