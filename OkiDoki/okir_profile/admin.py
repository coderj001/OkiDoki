from django.contrib import admin
from okir_profile.models import OkirProfile


@admin.register(OkirProfile)
class OkirProfileAdmin(admin.ModelAdmin):
    pass
