from django.contrib import admin

from distribution_platform.models import DistributionPlatform

@admin.register(DistributionPlatform)
class AdminDistributionPlatform(admin.ModelAdmin):
    pass
