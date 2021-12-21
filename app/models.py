from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date, Time
from sqlalchemy.orm import relationship
from .database import Base

class WGEWRaingage(Base):
    """Walnut Gulch Experimental Watershed raingage
    """

    __tablename__ = "wgew_raingages"

    id = Column(Integer, primary_key=True, index=True)
    gage_id = Column(Integer, unique=True, index=True)
    watershed_id = Column(Integer)
    east = Column(Integer)
    north = Column(Integer)
    elevation = Column(Integer)
    err = Column(Float)
    precip_events = relationship("WGEWPrecipEvent")

    def __repr__(self) -> str:
        return f"Raigage: {self.id}, gage_id: {self.gage_id}, watershed_id: {self.watershed_id}"

class WGEWPrecipEvent(Base):

    __tablename__ = "wgew_precip_events"

    id = Column(Integer, primary_key=True, index=True)
    gage_id = Column(Integer, ForeignKey('wgew_raingages.gage_id'))
    watershed_id = Column(Integer)
    event_date = Column(Date)
    event_time = Column(Time)
    duration = Column(Integer)
    depth = Column(Float)
    time_est = Column(String)

    def __repr__(self) -> str:
        return f"Precip Event: {self.id}, gage_id: {self.gage_id}, watershed_id: {self.watershed_id}"
