from typing import List, Optional
import graphql
from pydantic import BaseModel
import typing
import strawberry

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

@strawberry.type
class Query:

    @strawberry.field
    def health(self) -> str:
        return "ok"

schema = strawberry.Schema(Query)
