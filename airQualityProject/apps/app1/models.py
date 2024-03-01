import uuid

from django.db import models


# Create your models here.

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    fecha_carga = models.DateTimeField(auto_now_add=True)


class EVCHangingLocation(models.Model):
    station_name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.station_name


class responseAPiQuality(models.Model):
    date = models.TextField(max_length=200)
    aqi = models.TextField(max_length=100)
    category = models.TextField(max_length=200)
    red = models.TextField(max_length=100)
    blue = models.TextField(max_length=100)
    green = models.TextField(max_length=100)
    coName = models.TextField(max_length=200)
    coValue = models.TextField(max_length=200)
    coSource = models.TextField(max_length=200)
    coEffect = models.TextField(max_length=200)
    noName = models.TextField(max_length=200)
    noValue = models.TextField(max_length=200)
    noSource = models.TextField(max_length=200)
    noEffect = models.TextField(max_length=200)
    pm10Name = models.TextField(max_length=200)
    pm10Value = models.TextField(max_length=200)
    pm10Source = models.TextField(max_length=200)
    pm10Effect = models.TextField(max_length=200)
    generalPopulation = models.TextField(max_length=200)
    heartDiseasePopulation = models.TextField(max_length=200)
    children = models.TextField(max_length=200)
