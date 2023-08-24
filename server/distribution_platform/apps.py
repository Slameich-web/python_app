from django.apps import AppConfig


class DistributionPlatformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'distribution_platform'

    verbose_name = 'Платформы распространения'
    verbose_name_plural = 'Платформы распространения'
