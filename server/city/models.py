from django.db import models


class City(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')

    def __str__(self):
        return f'Город {self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
