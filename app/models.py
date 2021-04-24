import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.types import Date
from sqlalchemy.sql import func
from .database import Base

class WGEWRaingage(Base):
    __tablename__ = "wgew_raingage"

    id = Column(Integer, primary_key=True, index=True)

    created = Column(DateTime(timezone=True), server_default=func.now())

    updated = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return "<WGEWRaingage(id={}, created={}, updated={})>".format(self.id, self.created, self.updated)

        # return super().__repr__()

class WGEWPrecipEvent(Base):

    __tablename__ = "wgew_precipevent"

    id = Column(Integer, primary_key=True, index=True)

    created = Column(DateTime(timezone=True), server_default=func.now())

    updated = Column(DateTime(timezone=True), onupdate=func.now())

# DT = Column(DateTime(timezone=True), default=func.now())
# from django.db import models
#
#class BaseWgew(models.Model):
#
#    created = models.DateTimeField(auto_now_add=True)
#
#    updated = models.DateTimeField(auto_now=True)
#
#    class Meta:
#        abstract = True
#        db_tablespace = 'wgew'

# class Raingage(models.Model):
#     """Walnut Gulch experimental watershed raingage"""

#     gage_id = models.CharField(null=True, blank=True, max_length=125)

#     watershed_id = models.CharField(null=True, blank=True, max_length=5)

#     latitude = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=5)

#     longitude = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=5)

#     elevation = models.IntegerField(null=True, blank=True)

#     err = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)

#     created = models.DateTimeField(auto_now_add=True)

#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         app_label = 'wgew'
#         verbose_name = 'Raingage'
#         verbose_name_plural = 'Raingages'

#     def __repr__(self):
#         return u'{}'.format(self.id)

#     def __str__(self):
#         return u'{}'.format(self.gage_id)

#     def str(self):
#         return self.name

# class PrecipEvent(models.Model):

#     raingage = models.ForeignKey(Raingage, on_delete=models.CASCADE, db_index=True)

#     event_date = models.DateField(blank=True, null=True)

#     event_time = models.TimeField(blank=True, null=True)

#     duration = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=5)

#     depth = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=5)

#     time_est = models.CharField(null=True, blank=True, max_length=2, default=None)

#     class Meta:
#         app_label = 'wgew'
#         verbose_name = 'Precip Events'
#         verbose_name_plural = 'Precip Events'

