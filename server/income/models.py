from django.db import models

class Income(models.Model):
    calculation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата подсчета')
    total = models.FloatField(verbose_name='Итог')
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to='product.Product', on_delete=models.CASCADE, verbose_name='Продукт')
    product_count = models.IntegerField(verbose_name='Количество продаж')

    def __str__(self):
        return f'Доход пользователя {self.user}'

    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'
