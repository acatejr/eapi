from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Raingage, PrecipEvent
from .serializers import RaingageSerializer, PrecipEventSerializer


class HomeView(TemplateView):
    template_name = 'index.html'


class PrecipEventAPIView(APIView):

    def get(self, request, format=None):
        queryset = PrecipEvent.objects.all()
        serializer = PrecipEventSerializer(queryset, many=True)
        return Response(serializer.data)


class RaingageAPIView(APIView):

    def get(self, request, format=None):
        queryset = Raingage.objects.all()
        serializer = RaingageSerializer(queryset, many=True)
        return Response(serializer.data)


class PrecipEventList(generics.ListCreateAPIView):
    serializer_class = PrecipEventSerializer

    def get_queryset(self):
        qs = []

        if 'year' in self.kwargs and 'gagename' in self.kwargs:
            year = self.kwargs['year']
            gagename = self.kwargs['gagename']
            qs = PrecipEvent.objects.filter(year=year, raingage__name=gagename)

        return qs
