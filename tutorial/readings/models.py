from django.db import models

# Create your models here.


class Readings(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    time = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return (
            f"{self.__class__.__name__}({self.id=}, "
            f"{self.time=}"
            f"{self.temperature=}"
            f"{self.humidity=})"
        )
