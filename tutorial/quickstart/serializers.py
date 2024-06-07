from rest_framework import serializers

from .models import TempReading

class TempReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempReading
        fields = (
            "id",
            "time",
            "temperature",
            "humidity",
        )