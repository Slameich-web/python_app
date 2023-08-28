from django.contrib import admin

from mailings.models import Mailing


@admin.register(Mailing)
class AdminMailing(admin.ModelAdmin):
    pass
