from django.shortcuts import render
from rest_framework import generics
from barberia_app.models import Turno
from barberia_app.serializers import TurnoSerializer

# Create your views here.
class TurnoList(generics.ListCreateAPIView):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer

class TurnoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer