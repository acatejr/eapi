from django.urls import path
from graphene_django.views import GraphQLView
from .views import HomeView
from .views import RaingageAPIView, PrecipEventAPIView #, PrecipEventList

app_name = 'appwgew'
urlpatterns = [
    path(r'', HomeView.as_view()),
    path(r'api/wgew/v1.0/raingages', RaingageAPIView.as_view()),
    path(r'api/wgew/v1.0/precipevents', PrecipEventAPIView.as_view()),
]

# urlpatterns = [
#     path(r'graphql', GraphQLView.as_view(graphiql=True)),
#     path(r'api/srer/v1.0/precipevents/gagename/<str:gagename>/year/<int:year>', PrecipEventList.as_view()),
# ]
