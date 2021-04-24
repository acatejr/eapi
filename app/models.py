import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.types import Date
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from .database import Base

class WGEWRaingage(Base):
    __tablename__ = "wgew_raingage"

    id = Column(Integer, primary_key=True, index=True)

    created = Column(DateTime(timezone=True), server_default=func.now())

    updated = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return "<WGEWRaingage(id={}, created={}, updated={})>".format(self.id, self.created, self.updated)


class WGEWPrecipEvent(Base):

    __tablename__ = "wgew_precipevent"

    id = Column(Integer, primary_key=True, index=True)

    created = Column(DateTime(timezone=True), server_default=func.now())

    updated = Column(DateTime(timezone=True), onupdate=func.now())

    raingage_id = Column(Integer, ForeignKey('wgew_raingage.id'))

    raingage = relationship(
        WGEWRaingage,
        backref=backref(
            'precipevents', 
            uselist=True, 
            cascade='delete,all'
        )
    )

    def __repr__(self):
        return ""
