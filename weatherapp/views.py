from django.shortcuts import render
import requests
import json

# Create your views here.


def index(request):

    try:

        weather_object = {}

        city_name = request.GET.get('city_name', 'Mumbai')

        my_api_key = 'yourAPIKEY'

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={my_api_key}&units=metric"

        response = requests.request("GET", url).json()

        print(response)

        speed = "{:.2f}".format(1.6*response['wind']['speed'])

        if response["cod"] != 404:

            weather_object['temp'] = response['main']['temp']
            weather_object['temp_min'] = response['main']['temp_min']
            weather_object['temp_max'] = response['main']['temp_max']
            weather_object['pressure'] = response['main']['pressure']
            weather_object['humidity'] = response['main']['humidity']
            weather_object['wind_speed'] = speed
            weather_object['city_name'] = city_name
            weather_object['desc'] = response['weather'][0]['description']

            return render(request, 'weatherapp/index.html', {'weather_object': weather_object})

    except:

        return render(request, 'weatherapp/error.html',{'city_name':city_name})
