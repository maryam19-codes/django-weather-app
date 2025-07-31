import requests
from django.shortcuts import render

def weather_view(request):
    city = request.GET.get('city', 'Lahore')
    api_key = 'c0c47950c5e416de2c245db1c1da48d0'
  # Replace with your real OpenWeatherMap API key from https://openweathermap.org/api
    
    if api_key == 'YOUR_API_KEY':
        return render(request, 'weather.html', {
            'weather': {'error': 'Please configure your OpenWeatherMap API key in views.py'}
        })

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    weather_data = {}

    try:
        response = requests.get(url)
        data = response.json()

        if data.get('cod') == 200:
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data['error'] = 'City not found.'
    except Exception:
        weather_data['error'] = 'Error fetching data.'

    return render(request, 'weather.html', {'weather': weather_data})


# Create your views here.
