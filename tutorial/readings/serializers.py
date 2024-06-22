from rest_framework import serializers

from .models import Readings


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readings
        fields = (
            "id",
            "time",
            "temperature",
            "humidity",
        )
