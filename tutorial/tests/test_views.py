import json
from datetime import datetime

from django.test import TestCase
from readings.models import Readings


class ReadingListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_readings = 13

        for author_id in range(number_of_readings):
            Readings.objects.create(
                location=str(author_id),
                time=datetime.now().isoformat(),
                temperature=1.0,
                humidity=1.0,
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/readings/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/api/readings")
        self.assertEqual(response.status_code, 200)


class ReadingListApiTest(TestCase):
    def test_post_get(self):
        data = dict(
            location="test",
            time=datetime.now().isoformat(),
            temperature=1.0,
            humidity=1.0,
        )

        post_response = self.client.post(
            "/api/readings", json.dumps(data), content_type="application/json"
        )
        print(post_response.content)
        self.assertEqual(post_response.status_code, 201)

        get_response = self.client.get("/api/readings")
        self.assertEqual(get_response.status_code, 200)

        get_data = get_response.json()[0]
        get_data["time"] = datetime.fromisoformat(get_data["time"])
        print(get_data)
        self.assertDictContainsSubset(data, get_data)
