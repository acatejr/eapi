from django.db import models
from django.db.models import IntegerField, DecimalField, DateTimeField, TimeField, DateField, CharField

class BaseModel(models.Model):

    created = DateTimeField(auto_now_add=True)

    updated = DateTimeField(auto_now=True)

    class Meta:
        app_label = 'wgew'

class Raingage(BaseModel):
    """Domain model for WGEW raingage"""

    watershed_id = IntegerField(blank=True)
    
    gage_id = IntegerField(blank=True)
    
    east = IntegerField(blank=True, null=True)
    
    north = IntegerField(blank=True, null=True) 
    
    latitude = DecimalField(blank=True, null=True, max_digits=15, decimal_places=5)
    
    longitude = DecimalField(blank=True, null=True, max_digits=15, decimal_places=5)

    elevation = IntegerField(blank=True, null=True) 
    
    err = DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)

class PrecipEvent(BaseModel):
    """Domain model for WGEW precipt event"""
    
    event_date = DateField(blank=True, null=True)

    event_time = TimeField(blank=True, null=True)

    duration = DecimalField(blank=True, null=True, max_digits=15, decimal_places=5)

    depth = DecimalField(blank=True, null=True, max_digits=15, decimal_places=5)

    time_est = CharField(max_length=2, blank=True, null=True)

    rain_gage = models.ForeignKey(Raingage, blank=True, null=True, on_delete=models.CASCADE)

