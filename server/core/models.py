from django.db import models

from core.validators import validate_telegram_media_size


class TelegramMediaTypes(models.TextChoices):
    photo = 'photo'
    video = 'video'
    document = 'document'


class TelegramMedia(models.Model):
    telegram_id = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Telegram ID')
    type = models.CharField(choices=TelegramMediaTypes.choices, verbose_name='Тип вложения')
    file = models.FileField(upload_to='media/telegram', verbose_name='Файл', validators=[validate_telegram_media_size])

    def __str__(self):
        return f'{self.type} ({self.pk})'

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
