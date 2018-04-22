from django.contrib import admin
from .models import Raingage
from .models import PrecipEvent


class PrecipEventInline(admin.TabularInline):
    model = PrecipEvent


@admin.register(Raingage)
class RaingageAdmin(admin.ModelAdmin):
    list_display = ['id', 'watershed_id', 'gage_id', 'elevation', 'created', 'updated']
    list_filter = ['watershed_id', 'gage_id',]
    inlines = [PrecipEventInline]


@admin.register(PrecipEvent)
class PrecipEventAdmin(admin.ModelAdmin):
    list_display = ['id', 'raingage', 'event_date', 'event_time', 'depth']
    list_per_page = 15
