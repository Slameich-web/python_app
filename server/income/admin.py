from django.contrib import admin

from income.models import Income


@admin.register(Income)
class AdminIncome(admin.ModelAdmin):
    pass
