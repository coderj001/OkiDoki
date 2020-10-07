from django.contrib import admin
from feed.models import Oki


@admin.register(Oki)
class OkiAdmin(admin.ModelAdmin):
    pass
