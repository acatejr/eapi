from fastapi import FastAPI
from datetime import datetime
import graphene
from graphene import Schema, relay
from starlette.graphql import GraphQLApp
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import WGEWRaingage as WGEWRaingageModel
from .models import SRERRaingage as SRERRaingageModel
from .models import SRERPrecipEvent as SRERPrecipEventModel
from .models import WGEWPrecipEvent as WGEWPrecipEventModel
from app.database import db_session

db = db_session()

class SRERRaingage(SQLAlchemyObjectType):

    class Meta:
        model = SRERRaingageModel
        interfaces = (relay.Node,)

class SRERPrecipEvent(SQLAlchemyObjectType):

    class Meta:
        model = SRERPrecipEventModel
        interfaces = (relay.Node,)

class WGEWPrecipEvent(SQLAlchemyObjectType):

    class Meta:
        model = WGEWPrecipEventModel
        interfaces = (relay.Node,)

class WGEWRaingage(SQLAlchemyObjectType):

    class Meta:
        model = WGEWRaingageModel
        interfaces = (relay.Node,)
    
class Query(graphene.ObjectType):
    node = relay.Node.Field()

    status = graphene.String(status=graphene.String(), description="Status")

    get_wgew_raingage = graphene.Field(
        WGEWRaingage, 
        id=graphene.NonNull(graphene.Int), 
        description="Query for specific WGEW raingage"
    )

    get_all_wgew_raingages = graphene.List(
        WGEWRaingage, 
        description="Get all WGEW raingages"
    )

    get_wgew_raingage_precip_events = graphene.List(
        WGEWPrecipEvent, 
        id=graphene.NonNull(graphene.Int), 
        description="Query for a specific WGEW raingage's precip events"
    )

    get_all_srer_raingages = graphene.List(
        SRERRaingage,
        description='Ge all SRER raingages'
    )

    get_srer_raingage = graphene.Field(
        SRERRaingage, 
        id=graphene.NonNull(graphene.Int), 
        description="Query for specific SRER raingage"
    )

    get_srer_raingage_precip_events = graphene.List(
        SRERPrecipEvent, 
        id=graphene.NonNull(graphene.Int), 
        description="Query for a specific SRER raingage's precip events"
    )

    @staticmethod
    def resolve_status(self, info):
        return "{}".format(datetime.now())

    @staticmethod
    def resolve_get_wgew_raingage(self, info, id):
        rg = db.query(WGEWRaingageModel).filter_by(id=id).first()
        return rg

    @staticmethod
    def resolve_get_all_wgew_raingages(self, info):
        gages = db.query(WGEWRaingageModel).all()
        return gages

    @staticmethod
    def resolve_get_wgew_raingage_precip_events(self, info, id):
        precip_events = db.query(WGEWPrecipEventModel).filter_by(raingage_id=id).all()
        return precip_events

    @staticmethod
    def resolve_get_all_srer_raingages(self, info):
        gages = db.query(SRERRaingageModel).all()
        return gages

    @staticmethod
    def resolve_get_srer_raingage(self, info, id):
        rg = db.query(SRERRaingageModel).filter_by(id=id).first()
        return rg

    @staticmethod
    def resolve_get_srer_raingage_precip_events(self, info, id):
        precip_events = db.query(SRERPrecipEventModel).filter_by(raingage_id=id).all()
        return precip_events

schema = Schema(query=Query)

app = FastAPI()

@app.get("/")
async def read_index():
    return {"msg": "Hello World"}

app.add_route(
    "/graphiql", 
    GraphQLApp(schema=schema)
)
