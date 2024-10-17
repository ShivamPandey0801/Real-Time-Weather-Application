from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from django.conf import settings

def get_weather(city):
    api_key = settings.WEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    print(f"Request URL: {response.url}")  # Print the full request URL
    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def weather_view(request):
    city = request.GET.get('city', 'London')  # we will take London as the Default city for the portal
    weather_data = get_weather(city)
    context = {'weather': weather_data}
    return render(request, 'weatherapplication/weather.html', context)