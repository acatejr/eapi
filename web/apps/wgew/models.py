from django.db import models
from django.db.models import IntegerField, DecimalField, DateTimeField

class BaseModel(models.Model):

    created = DateTimeField(auto_now_add=True)

    updated = DateTimeField(auto_now=True)

    class Meta:
        app_label = 'wgew'
        # db_tablespace = 'wgew'

class Raingage(BaseModel):
    """Domain model for WGEW raingage"""

    watershed_id = IntegerField(blank=True)
    
    gage_id = IntegerField(blank=True)
    
    east = IntegerField(blank=True)
    
    north = IntegerField(blank=True) 
    
    latitude = DecimalField(blank=True, max_digits=15, decimal_places=5)
    
    longitude = DecimalField(blank=True, max_digits=15, decimal_places=5)

    elevation = IntegerField(blank=True) 
    
    err = DecimalField(blank=True, max_digits=5, decimal_places=1)
