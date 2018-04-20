import graphene
from graphene import Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import django_filters

from .models import Raingage as RaingageModel
from .models import PrecipEvent as PrecipEventModel


class Raingage(DjangoObjectType):
    class Meta:
        model = RaingageModel
        interfaces = (Node, )


class PrecipEvent(DjangoObjectType):
    class Meta:
        model = PrecipEventModel
        interfaces = (Node, )


class PrecipEventFilterSet(django_filters.FilterSet):
    year = django_filters.NumberFilter()

    class Meta:
        model = PrecipEventModel
        fields = ['year', 'raingage__name']


class Query(graphene.ObjectType):
    raingages = graphene.List(Raingage)
    precipevents = DjangoFilterConnectionField(PrecipEvent,filterset_class=PrecipEventFilterSet)

    @staticmethod
    def resolve_raingages(self, info):
        qs = RaingageModel.objects.all()
        return qs

    @staticmethod
    def resolve_precipevents(self, info, **kwargs):
        objs = []

        if 'year' in kwargs and 'raingage__name' in kwargs:
            yr = int(kwargs['year'])
            gage_name = kwargs['raingage__name']
            objs = PrecipEventModel.objects.filter(year=yr, raingage__name=gage_name)

        return objs


schema = graphene.Schema(query=Query)
