from datetime import datetime

from django.test import TestCase
from readings.models import Readings


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Readings.objects.create(
            location="test",
            time=datetime.now().isoformat(),
            temperature=1.0,
            humidity=1.0,
        )

    def test_id_generation(self):
        reading = Readings.objects.all()[0]
        assert isinstance(reading.id, str) and reading.id != ""

    def test_str(self):
        reading = Readings.objects.all()[0]
        assert isinstance(str(reading), str)
