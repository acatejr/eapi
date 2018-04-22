from django.contrib import admin
from .models import Raingage, PrecipEvent


admin.site.site_header = 'EAPI'
admin.site.index_title = 'Modules'
admin.site.site_title = 'EAPI Adminsitration'


class PrecipEventInline(admin.TabularInline):
    model = PrecipEvent


@admin.register(Raingage)
class RaingageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'created', 'updated']
    inlines = [PrecipEventInline]


@admin.register(PrecipEvent)
class PrecipEventAdmin(admin.ModelAdmin):
    list_display = ['id', 'raingage', 'year', 'month', 'precip']
    list_per_page = 15

