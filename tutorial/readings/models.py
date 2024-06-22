from django.db import models
import uuid


class Readings(models.Model):
    id = models.CharField(max_length=100, primary_key=True, blank=True)
    location = models.CharField(max_length=20)
    time = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()

    @property
    def get_id(self):
        return str(uuid.uuid4())

    def save(self, *args, **kwargs):
        self.id = self.get_id
        super(Readings, self).save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.__class__.__name__}({self.id=}, "
            f"{self.time=}"
            f"{self.temperature=}"
            f"{self.humidity=})"
        )
