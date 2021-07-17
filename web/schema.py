import graphene
from graphene_django import DjangoObjectType

from apps.wgew.models import Raingage as WGEWRaingage


class WGEWRaingageType(DjangoObjectType):

    class Meta:
        description = 'WGEW Raingage'
        model = WGEWRaingage
        fields = ('id', 'watershed_id', 'gage_id', 'east', 'north', 'latitude', 'longitude', 'elevation', 'err') 

class Query(graphene.ObjectType):
    """Returns all WGEW raingages"""
    all_wgew_raingages = graphene.List(WGEWRaingageType, description="Walnut Gulch Exerimental Watershed Raingage")

    def resolve_all_wgew_raingages(root, info):
        return WGEWRaingage.objects.all()


schema = graphene.Schema(query=Query)

