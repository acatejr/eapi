from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

class WGEWRaingage(Base):
    """Walnut Gulch Experimental Watershed raingage
    """

    __tablename__ = "wgew_raingages"

    id = Column(Integer, primary_key=True, index=True)
    gage_id = Column(Integer)
    watershed_id = Column(Integer)
    east = Column(Integer)
    north = Column(Integer)
    elevation = Column(Integer)
    err = Column(Float)

# class User(Base):

#     __tablename__ = "users"


#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")



# class Item(Base):

#     __tablename__ = "items"


#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")
