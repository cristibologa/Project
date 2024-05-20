from django.shortcuts import render
import requests
from .models import City

from django.shortcuts import render, redirect
import requests

from .forms import CityForm


def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

    cities = City.objects.all()
    API = 'b66950987d030ebc606502fe356ae33f'
    if request.method == 'POST':

        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city, API)).json()

        weather = {
            'city': city,
            'temperature': round((city_weather['main']['temp']-32)/1.8),
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)


def delete_city(request, city_name):
    city = City.objects.filter(name=city_name).order_by('id').first()
    city.delete()
    return redirect('index')
