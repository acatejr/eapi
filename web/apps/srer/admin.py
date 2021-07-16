from django.contrib import admin

from .models import Raingage
from .models import PrecipEvent

@admin.register(Raingage)
class RaingageAdmin(admin.ModelAdmin):
    list_display = ('id', 'station_code', 'current_station_name', 'created', 'updated')

@admin.register(PrecipEvent)
class PrecipEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'month', 'rain_gage', 'created', 'updated')
