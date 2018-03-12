"""
Domain models for the Santa Rita Experimental Range
"""
from __future__ import unicode_literals
from django.contrib.gis.db import models


class Raingage(models.Model):
    """ Raingage domain model.
    """

    # The station code
    code = models.CharField(null=False, blank=False, unique=True, max_length=150)

    # The current station name
    name = models.CharField(null=False, blank=False, unique=True, max_length=150)

    # location = models.PointField(blank=True, null=True, srid=4326)
    latitude = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=5)

    longitude = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=5)

    created = models.DateTimeField(auto_now_add=True, editable=False)

    updated = models.DateTimeField(auto_now=True)

    # def latitude(self):
    #     return self.location.y
    #
    # def longitude(self):
    #     return self.location.x

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        """ Meta attributes """

        app_label = 'appeapi'
        verbose_name = 'Raingage'


class PrecipEvent(models.Model):

    MONTH_CHOICES = [
        ['JAN', 'JAN'],
        ['FEB', 'FEB'],
        ['MAR', 'MAR'],
        ['APR', 'APR'],
        ['MAY', 'MAY'],
        ['JUN', 'JUN'],
        ['JUL', 'JUL'],
        ['AUG', 'AUG'],
        ['SEP', 'SEP'],
        ['OCT', 'OCT'],
        ['NOV', 'NOV'],
        ['DEC', 'DEC'],
    ]

    raingage = models.ForeignKey(Raingage, related_name='precip_events', on_delete=models.CASCADE)

    year = models.IntegerField(null=True, blank=True)

    month = models.CharField(null=True, blank=True, max_length=3, choices=MONTH_CHOICES)

    precip = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=5)

    created = models.DateTimeField(auto_now_add=True, editable=False)

    updated = models.DateTimeField(auto_now=True)

    def raingage_name(self):
        return u"{}".format(self.raingage.name)

    class Meta:
        app_label = 'appeapi'
        verbose_name = 'Precip Event'

