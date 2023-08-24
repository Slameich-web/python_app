from django.contrib import admin

from mailing.models import Mailing


@admin.register(Mailing)
class AdminMailing(admin.ModelAdmin):
    pass
