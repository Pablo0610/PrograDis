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
    date = models.TextField(max_length=200,null=True)
    aqi = models.TextField(max_length=100,null=True)
    category = models.TextField(max_length=200,null=True)
    red = models.TextField(max_length=100,null=True)
    blue = models.TextField(max_length=100,null=True)
    green = models.TextField(max_length=100,null=True)
    coName = models.TextField(max_length=200,null=True)
    coValue = models.TextField(max_length=200,null=True)
    coSource = models.TextField(max_length=200,null=True)
    coEffect = models.TextField(max_length=200,null=True)
    noName = models.TextField(max_length=200,null=True)
    noValue = models.TextField(max_length=200,null=True)
    noSource = models.TextField(max_length=200,null=True)
    noEffect = models.TextField(max_length=200,null=True)
    pm10Name = models.TextField(max_length=200,null=True)
    pm10Value = models.TextField(max_length=200,null=True)
    pm10Source = models.TextField(max_length=200,null=True)
    pm10Effect = models.TextField(max_length=200,null=True)
    so2Name = models.TextField(max_length=200,null=True)
    so2Value = models.TextField(max_length=200,null=True)
    so2Source = models.TextField(max_length=200,null=True)
    so2Effect = models.TextField(max_length=200,null=True)
    pm25Name = models.TextField(max_length=200,null=True)
    pm25Value = models.TextField(max_length=200,null=True)
    pm25Source = models.TextField(max_length=200,null=True)
    pm25Effect = models.TextField(max_length=200,null=True)
    generalPopulation = models.TextField(max_length=200,null=True)
    heartDiseasePopulation = models.TextField(max_length=200,null=True)
    children = models.TextField(max_length=200,null=True)
