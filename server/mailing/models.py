from django.db import models


class Mailing(models.Model):
    message = models.TextField(verbose_name='Текст сообщения')
    attachment = models.ForeignKey(to='core.TelegramMedia', on_delete=models.SET_NULL, null=True,
                                   verbose_name='Вложение')
    start_time = models.DateTimeField(verbose_name='Время')

    def __str__(self):
        return f'Рассылка ({self.start_time})'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
