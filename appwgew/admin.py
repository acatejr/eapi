from django.contrib import admin
from .models import Raingage
# from .models import PrecipEvent


admin.site.site_header = 'EAPI'
admin.site.index_title = 'Modules'
admin.site.site_title = 'WGEW EAPI Adminsitration'

@admin.register(Raingage)
class RaingageAdmin(admin.ModelAdmin):
    list_display = ['id', 'watershed_id', 'gage_id', 'elevation', 'created', 'updated']
    list_filter = ['watershed_id', 'gage_id',]
    # inlines = [PrecipEventInline]

