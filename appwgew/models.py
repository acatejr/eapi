from django.db import models

class BaseWgew(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        db_tablespace = 'wgew'


class Raingage(BaseWgew):

    watershed_id = models.CharField(null=True, blank=True, max_length=5)

    gage_id = models.CharField(null=True, blank=True, max_length=125)

    latitude = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=5)

    longitude = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=5)

    elevation = models.IntegerField(null=True, blank=True)

    err = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)

    class Meta:
        app_label = 'appwgew'
        verbose_name = 'Raingage'
        verbose_name_plural = 'Raingages'

    def __repr__(self):
        return u'{}'.format(self.id)

    def __str__(self):
        return u'{}'.format(self.gage_id)

    def str(self):
        return self.name


class PrecipEvent(BaseWgew):

    raingage = models.ForeignKey(Raingage, on_delete=models.CASCADE, db_index=True)

    event_date = models.DateField(blank=True, null=True)

    event_time = models.TimeField(blank=True, null=True)

    duration = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=5)

    depth = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=5)

    time_est = models.CharField(null=True, blank=True, max_length=2, default=None)

    class Meta:
        app_label = 'appwgew'
        verbose_name = 'Precip Events'
        verbose_name_plural = 'Precip Events'
