from django.apps import AppConfig


class CityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'city'

    verbose_name = 'Города'
    verbose_name_plural = 'Города'