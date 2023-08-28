from django.urls import path
from rest_framework.routers import DefaultRouter

from core.views import BotSettingsView, UpdateTelegramMediaView

router = DefaultRouter()

router.register('media/update', UpdateTelegramMediaView, basename='update_telegram_media')

urlpatterns = [
    path('bot_settings', BotSettingsView.as_view(), name='core_bot_settings')
] + router.get_urls()
