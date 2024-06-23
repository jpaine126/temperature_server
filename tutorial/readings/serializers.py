from rest_framework import serializers

from .models import Readings


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readings
        fields = (
            "id",
            "location",
            "time",
            "temperature",
            "humidity",
        )
