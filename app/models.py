import datetime
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, Time
from sqlalchemy.types import Date
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from .database import Base

class WGEWRaingage(Base):
    __tablename__ = "wgew_raingage"

    id = Column(Integer, primary_key=True, index=True)

    watershed_id = Column(Integer(), nullable=True)

    gage_id = Column(Integer(), nullable=True)

    east = Column(Integer(), nullable=True)

    north = Column(Integer(), nullable=True)

    latitude = Column(Numeric(precision=15, scale=5), nullable=True)

    longitude = Column(Numeric(precision=15, scale=5), nullable=True)

    elevation = Column(Integer(), nullable=True)

    err = Column(Numeric(precision=5, scale=1), nullable=True)

    created = Column(DateTime(timezone=True), server_default=func.now())

    updated = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return "<WGEWRaingage(id={}, created={}, updated={})>".format(self.id, self.created, self.updated)


class WGEWPrecipEvent(Base):

    __tablename__ = "wgew_precipevent"

    id = Column(Integer, primary_key=True, index=True)

    event_date = Column(DateTime(timezone=True))

    event_time = Column(Time(timezone=True))    

    duration = Column(Numeric(precision=15, scale=5), nullable=True)

    depth = Column(Numeric(precision=15, scale=5), nullable=True)

    time_est = Column(String(length=2), nullable=True)

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
