from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import TempReading
from .serializers import TempReadingSerializer


class TempReadingList(generics.ListCreateAPIView):
    queryset = TempReading.objects.all()
    serializer_class = TempReadingSerializer


class TempReadingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TempReading.objects.all()
    serializer_class = TempReadingSerializer