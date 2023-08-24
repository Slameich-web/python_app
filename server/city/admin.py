from django.contrib import admin

from city.models import City


@admin.register(City)
class AdminCity(admin.ModelAdmin):
    pass
