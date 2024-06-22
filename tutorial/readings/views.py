from django.http.response import JsonResponse
from django.shortcuts import render
# Create your views here.
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Readings
from .serializers import ReadingSerializer


@api_view(["GET", "POST"])
def api_root(request):
    if request.method == "GET":
        readings = Readings.objects.all()
        readings_serializer = ReadingSerializer(readings, many=True)
        return JsonResponse(readings_serializer.data, safe=False)
    elif request.method == "POST":
        reading_data = JSONParser().parse(request)
        reading_serializer = ReadingSerializer(data=reading_data)

        if reading_serializer.is_valid():
            reading_serializer.save()
            return JsonResponse(reading_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(reading_serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ReadingList(generics.ListCreateAPIView):
    queryset = Readings.objects.all()
    serializer_class = ReadingSerializer


class ReadingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Readings.objects.all()
    serializer_class = ReadingSerializer
