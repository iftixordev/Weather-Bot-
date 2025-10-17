import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5'

# O'zbekiston shaharlari
UZBEKISTAN_CITIES = {
    'Toshkent': 'Tashkent',
    'Samarqand': 'Samarkand', 
    'Buxoro': 'Bukhara',
    'Andijon': 'Andijan',
    'Farg\'ona': 'Fergana',
    'Namangan': 'Namangan',
    'Qashqadaryo': 'Qarshi',
    'Surxondaryo': 'Termez',
    'Jizzax': 'Jizzakh',
    'Sirdaryo': 'Gulistan',
    'Navoiy': 'Navoi',
    'Xorazm': 'Urgench',
    'Qoraqalpog\'iston': 'Nukus'
}

# Emoji ikonkalar
WEATHER_ICONS = {
    'clear sky': '☀️',
    'few clouds': '🌤️',
    'scattered clouds': '⛅',
    'broken clouds': '☁️',
    'shower rain': '🌦️',
    'rain': '🌧️',
    'thunderstorm': '⛈️',
    'snow': '❄️',
    'mist': '🌫️'
}