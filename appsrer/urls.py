from django.urls import path
from graphene_django.views import GraphQLView
#from .views import RaingageAPIView, PrecipEventAPIView, HomeView, PrecipEventList

app_name = 'appsrer'
urlpatterns = [
    path(r'graphql', GraphQLView.as_view(graphiql=True)),
    # path(r'api/srer/v1.0/raingages', RaingageAPIView.as_view()),
    # path(r'api/srer/v1.0/precipevents', PrecipEventAPIView.as_view()),
    # path(r'api/srer/v1.0/precipevents/gagename/<str:gagename>/year/<int:year>', PrecipEventList.as_view()),
]
