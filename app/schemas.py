from datetime import date
from pydantic import BaseModel


class Raingage(BaseModel):
    id: int
    # date: date
    # country: str
    # cases: int
    # deaths: int
    # recoveries: int

    class Config:
        orm_mode = True