from django.db import models

class BaseWgew(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        db_tablespace = 'wgew'

class Raingage(models.Model):
    """Walnut Gulch experimental watershed raingage"""

    gage_id = models.CharField(null=True, blank=True, max_length=125)

    watershed_id = models.CharField(null=True, blank=True, max_length=5)

    latitude = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=5)

    longitude = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=5)

    elevation = models.IntegerField(null=True, blank=True)

    err = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'wgew'
        verbose_name = 'Raingage'
        verbose_name_plural = 'Raingages'

    def __repr__(self):
        return u'{}'.format(self.id)

    def __str__(self):
        return u'{}'.format(self.gage_id)

    def str(self):
        return self.name
