from typing import List, Optional
from pydantic import BaseModel

class WGEWRaingageBase(BaseModel):
    pass

class WGEWRaingage(WGEWRaingageBase):
    id: int

    class Config:
        orm_mode = True