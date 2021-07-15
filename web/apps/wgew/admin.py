from django.contrib import admin

from .models import Raingage
from .models import PrecipEvent

@admin.register(Raingage)
class RaingageAdmin(admin.ModelAdmin):
    list_display = ('id', 'gage_id', 'created', 'updated')

@admin.register(PrecipEvent)
class PrecipEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'updated')

