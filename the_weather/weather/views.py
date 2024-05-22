from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
from django.contrib import messages


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    API_KEY = 'b66950987d030ebc606502fe356ae33f'

    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            if not City.objects.filter(name=new_city).exists():
                response = requests.get(url.format(new_city, API_KEY))
                if response.status_code == 200:
                    form.save()
                else:
                    messages.error(
                        request, 'Așa orașul nu există')
            else:
                messages.warning(
                    request, 'Orașul deja este in baza de date')
        else:
            messages.error(request, 'Numele nu este valid')

    form = CityForm()
    weather_data = []

    for city in cities:
        response = requests.get(url.format(city.name, API_KEY))
        if response.status_code == 200:
            city_weather = response.json()
            weather = {
                'city': city.name,
                'temperature': round((city_weather['main']['temp'] - 32) / 1.8),
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)
        else:
            messages.error(
                request, f'Eroare la preluarea datelor meteo pentru {city.name}')

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/index.html', context)


def delete_city(request, city_name):
    city = City.objects.filter(name=city_name).first()
    city.delete()
    messages.success(request, f'{city_name} has been deleted.')
    return redirect('index')
