from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=256, verbose_name='Название')
    cost = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return f'Продукт {self.name}'
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
