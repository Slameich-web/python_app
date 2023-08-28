from django.contrib import admin
from core.models import BotSettings, TelegramMedia


@admin.register(BotSettings)
class AdminBotSettings(admin.ModelAdmin):
    list_display = ('start_message',)

    def has_add_permission(self, request):
        return not len(BotSettings.objects.all())

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TelegramMedia)
class AdminTelegramMedia(admin.ModelAdmin):
    # exclude = ('telegram_id', 'id')
    pass