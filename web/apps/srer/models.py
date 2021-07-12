from django.db import models
from django.db.models import IntegerField, DecimalField, DateTimeField, TimeField, DateField, CharField

class SRERBaseModel(models.Model):

    created = DateTimeField(auto_now_add=True)

    updated = DateTimeField(auto_now=True)

    class Meta:
        app_label = 'srer'

class Raingage(SRERBaseModel):
    
    station_code = CharField(blank=True, null=True, max_length=25) 

    current_station_name = CharField(blank=True, null=True, max_length=25)

    latitude = DecimalField(blank=True, null=True, max_digits=15, decimal_places=5)
         
    longitude = DecimalField(blank=True, null=True, max_digits=15, decimal_places=5)

class PrecipEvent(SRERBaseModel):

    year = IntegerField(blank=True, null=True)

    month = IntegerField(blank=True, null=True)

    precip = DecimalField(blank=True, null=True, max_digits=15, decimal_places=5)

    rain_gage = models.ForeignKey(Raingage, blank=True, null=True, on_delete=models.CASCADE)

