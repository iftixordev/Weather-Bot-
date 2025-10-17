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
    'overcast clouds': '☁️',
    'shower rain': '🌦️',
    'rain': '🌧️',
    'light rain': '🌦️',
    'moderate rain': '🌧️',
    'heavy intensity rain': '🌧️',
    'thunderstorm': '⛈️',
    'snow': '❄️',
    'mist': '🌫️',
    'fog': '🌫️',
    'haze': '🌫️',
    'smoke': '💨',
    'dust': '🌪️',
    'sand': '🌪️',
    'ash': '🌋',
    'squall': '💨',
    'tornado': '🌪️',
    'drizzle': '🌦️'
}

# O'zbek tiliga tarjima
WEATHER_TRANSLATIONS = {
    'clear sky': 'ochiq osmon',
    'few clouds': 'oz bulutli',
    'scattered clouds': 'tarqoq bulutlar',
    'broken clouds': 'bulutli',
    'overcast clouds': 'bulutli',
    'shower rain': 'yomg\'ir',
    'rain': 'yomg\'ir',
    'light rain': 'engil yomg\'ir',
    'moderate rain': 'o\'rtacha yomg\'ir',
    'heavy intensity rain': 'kuchli yomg\'ir',
    'thunderstorm': 'momaqaldiroq',
    'snow': 'qor',
    'mist': 'tuman',
    'fog': 'tuman',
    'haze': 'tuman',
    'smoke': 'tutun',
    'dust': 'chang',
    'sand': 'qum',
    'ash': 'kul',
    'squall': 'bo\'ron',
    'tornado': 'tornado',
    'drizzle': 'mayda yomg\'ir'
}