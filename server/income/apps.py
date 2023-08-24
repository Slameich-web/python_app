from django.apps import AppConfig


class IncomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'income'

    verbose_name = 'Доходы'
    verbose_name_plural = 'Доходы'
