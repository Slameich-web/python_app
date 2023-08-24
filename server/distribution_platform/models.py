from django.db import models

class DistributionPlatform(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')

    def __str__(self):
        return f'Платформа распространения {self.name}'

    class Meta:
        verbose_name = 'Платформа распространения'
        verbose_name_plural = 'Платформы распространения'
