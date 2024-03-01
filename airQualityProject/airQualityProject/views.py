import json
import smtplib
from email.message import EmailMessage

import requests
from apps.app1.models import EVCHangingLocation, responseAPiQuality
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import Context

base_url = "https://airquality.googleapis.com/v1/currentConditions:lookup?key="
api_key = "AIzaSyDveBq8p4Zf7xp1jraj3Y4JRutrnSM47bk"


def welcome_page(request):
    return HttpResponse("welcome page")


def airQualityPage(request):
    return render(request, 'index.html')


def nearest_station(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    EVCHangingLocation.objects.all().delete()
    a = EVCHangingLocation.objects.create(latitude=latitude, longitude=longitude)
    # print(latitude, longitude)
    print(a)
    return JsonResponse({})


def metter_value(request):
    getValuesApi()
    responseAPI = responseAPiQuality.objects.latest('id')
    print(responseAPI.date)
    context = {'responseAPI': responseAPI}
    return render(request, 'index.html', context)


def getValuesApi():
    url = base_url + api_key
    coordinates = EVCHangingLocation.objects.latest('id')
    myobj = {
        "universalAqi": 'true',
        "location": {
            "latitude": coordinates.latitude,
            "longitude": coordinates.longitude
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
        so2Name=x['pollutants'][4]['fullName'],
        so2Value=x['pollutants'][4]['concentration']['value'],
        so2Source=x['pollutants'][4]['additionalInfo']['sources'],
        so2Effect=x['pollutants'][4]['additionalInfo']['effects'],
        pm25Name=x['pollutants'][5]['fullName'],
        pm25Value=x['pollutants'][5]['concentration']['value'],
        pm25Source=x['pollutants'][5]['additionalInfo']['sources'],
        pm25Effect=x['pollutants'][5]['additionalInfo']['effects'],
        generalPopulation=x['healthRecommendations']['generalPopulation'],
        heartDiseasePopulation=x['healthRecommendations']['heartDiseasePopulation'],
        children=x['healthRecommendations']['children']
    )

def send_mail(request):
    # import smtplib
    msg = EmailMessage()
    msg['Subject'] = 'Air Quality Pollution'
    msg['From'] = 'jchristian@gmail.com'
    msg['To'] = request.GET["email"]
    msg.set_content('Mensaje de prueba')
    print(msg)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)
    server.login('jchristian@gmail.com', 'l')  # user & password
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail.')
    return render(request, 'index.html')
