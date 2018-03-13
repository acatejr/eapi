from django.contrib import admin
from .models import PrecipEvent, Raingage

admin.site.index_title = "Administration"
admin.site.site_header = "Administration"


class PrecipEventInline(admin.TabularInline):
    model = PrecipEvent


@admin.register(Raingage)
class RaingageAdmin(admin.ModelAdmin):
    default_lat = 31.6445225
    default_lon = -110.8707519
    default_zoom = 7
    wms_url = "http://ows.terrestris.de/osm/service"
    wms_layer = "TOPO-OSM-WMS"
    list_display = ['id', 'name', 'latitude', 'longitude', 'created', 'updated']
    inlines = [PrecipEventInline,]


@admin.register(PrecipEvent)
class PrecipEvent(admin.ModelAdmin):
    list_display = ['id', 'raingage_name', 'month', 'year', 'precip', 'created', 'updated']
