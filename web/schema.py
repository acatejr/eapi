import graphene
from graphene_django import DjangoObjectType

from apps.wgew.models import Raingage as WGEWRaingage
from apps.srer.models import Raingage as SRERRaingage

class SRERRaingageType(DjangoObjectType):

    class Meta:
        description = 'SRER Raingage'
        model = SRERRaingage

class WGEWRaingageType(DjangoObjectType):

    class Meta:
        description = 'WGEW Raingage'
        model = WGEWRaingage
        fields = ('id', 'watershed_id', 'gage_id', 'east', 'north', 'latitude', 'longitude', 'elevation', 'err') 

class Query(graphene.ObjectType):
    """Returns all WGEW raingages"""
    all_wgew_raingages = graphene.List(WGEWRaingageType, description="Walnut Gulch Exerimental Watershed Raingage")
    all_srer_raingages = graphene.List(SRERRaingageType, description="Santa Rita Experimental Range Raingage")

    def resolve_all_wgew_raingages(root, info):
        return WGEWRaingage.objects.all()

    def resolve_all_srer_raingages(root, info):
        return SRERRaingage.objects.all()


schema = graphene.Schema(query=Query)

