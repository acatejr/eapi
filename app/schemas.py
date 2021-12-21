from typing import List, Optional
from pydantic import BaseModel

class WGEWRaingageBase(BaseModel):
    pass

class WGEWRaingage(WGEWRaingageBase):
    id: int
    watershed_id: int
    gage_id: int
    east: int
    north: int
    elevation: int
    err: float

    class Config:
        orm_mode = True