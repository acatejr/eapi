from django.urls import path
from graphene_django.views import GraphQLView
from .views import HomeView
from .views import RaingageAPIView, PrecipEventAPIView #, PrecipEventList
from .schema import schema


app_name = 'appwgew'
urlpatterns = [
    path(r'', HomeView.as_view(), name='home'),
    path(r'api/wgew/v1.0/raingages', RaingageAPIView.as_view()),
    path(r'api/wgew/v1.0/precipevents', PrecipEventAPIView.as_view()),
    path(r'graphql', GraphQLView.as_view(graphiql=True, schema=schema), name='wgew_graphql'),
]
