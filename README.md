# Weather App

A simple Django weather application that fetches weather data using the OpenWeatherMap API.

## Features

- Search weather by city name
- Display temperature in Celsius
- Show weather description and icon
- Responsive design with modern UI

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get OpenWeatherMap API Key

1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Get your API key from your account dashboard

### 3. Configure API Key

Open `weatherapp/views.py` and replace `'YOUR_API_KEY'` with your actual API key:

```python
api_key = 'your_actual_api_key_here'
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

### 6. Access the Application

Open your browser and go to `http://127.0.0.1:8000/`

## Usage

1. Enter a city name in the search box
2. Click "Get Weather" button
3. View the current weather information including temperature, description, and weather icon

## Project Structure

```
weatherapp_project/
├── manage.py
├── requirements.txt
├── README.md
├── weatherapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── weather.html
└── weatherproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

## Dependencies

- Django >= 5.2.4
- requests >= 2.31.0

## Notes

- The app uses the free tier of OpenWeatherMap API
- Weather data is fetched in real-time
- Temperature is displayed in Celsius
- The app includes error handling for invalid cities and API issues 