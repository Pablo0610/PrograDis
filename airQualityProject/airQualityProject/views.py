import json

import requests
from apps.app1.models import EVCHangingLocation, responseAPiQuality
from django.http import HttpResponse, JsonResponse
from django.shortcuts import reverse, redirect,render
from django.template import Template, Context

base_url = "https://airquality.googleapis.com/v1/currentConditions:lookup?key="
api_key = "AIzaSyDveBq8p4Zf7xp1jraj3Y4JRutrnSM47bk"


def welcome_page(request):
    return HttpResponse("welcome page")


def airQualityPage(request):
    tmp = open(
        "/home/chrisubuntu/PycharmProjects/airQualityProject/airQualityProject/airQualityProject/templates/index.html")
    template = Template(tmp.read())
    tmp.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)


def nearest_station(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    EVCHangingLocation.objects.all().delete()
    a = EVCHangingLocation.objects.create(latitude=latitude, longitude=longitude)
    # print(latitude, longitude)
    print(a)
    return JsonResponse({})


def metter_value(request):
    tmp = open(
        "/home/chrisubuntu/PycharmProjects/airQualityProject/airQualityProject/airQualityProject/templates/index.html")
    template = Template(tmp.read())
    tmp.close()
    context = Context()
    document = template.render(context)
    getValuesApi()
    responseAPI = responseAPiQuality.objects.latest('id')
    print(responseAPI.date)
    context = {'responseAPI': responseAPI}
    return render(request, 'index.html', context)


def getValuesApi():
    url = base_url + api_key
    myobj = {
        "universalAqi": 'true',
        "location": {
            "latitude": 37.419734,
            "longitude": -122.0827784
        },
        "extraComputations": [
            "HEALTH_RECOMMENDATIONS",
            "DOMINANT_POLLUTANT_CONCENTRATION",
            "POLLUTANT_CONCENTRATION",
            "LOCAL_AQI",
            "POLLUTANT_ADDITIONAL_INFO"
        ],
        "languageCode": "es"
    }
    response = requests.request("POST", url, json=myobj)
    x = json.loads(response.text)
    # print(x['pollutants'][0]['additionalInfo']['sources'])
    # print(response.json())
    responseAPiQuality.objects.all().delete()
    responseAPiQuality.objects.create(
        date=x['dateTime'],
        aqi=x['indexes'][0]['aqi'],
        category=x['indexes'][0]['category'],
        red=x['indexes'][0]['color']['red'],
        blue=x['indexes'][0]['color']['green'],
        green=x['indexes'][0]['color']['blue'],
        coName=x['pollutants'][0]['fullName'],
        coValue=x['pollutants'][0]['concentration']['value'],
        coSource=x['pollutants'][0]['additionalInfo']['sources'],
        coEffect=x['pollutants'][0]['additionalInfo']['effects'],
        noName=x['pollutants'][1]['fullName'],
        noValue=x['pollutants'][1]['concentration']['value'],
        noSource=x['pollutants'][1]['additionalInfo']['sources'],
        noEffect=x['pollutants'][1]['additionalInfo']['effects'],
        pm10Name=x['pollutants'][3]['fullName'],
        pm10Value=x['pollutants'][3]['concentration']['value'],
        pm10Source=x['pollutants'][3]['additionalInfo']['sources'],
        pm10Effect=x['pollutants'][3]['additionalInfo']['effects'],
        generalPopulation=x['healthRecommendations']['generalPopulation'],
        heartDiseasePopulation=x['healthRecommendations']['heartDiseasePopulation'],
        children=x['healthRecommendations']['children']
    )
