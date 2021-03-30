from django.db import models

# Create your models here.

class Raingage(models.Model):
    """watershed_id|gage_id|east|north|elevation|err"""

    gage_id = models.IntegerField()
    # east = models.IntegerField()
    # north = models.IntegerField()
    # elevation = models.DecimalField()
    # err = models.

