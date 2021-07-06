from django.contrib import admin
from .models import Raingage

@admin.register(Raingage)
class RaingageAdmin(admin.ModelAdmin):
    pass
