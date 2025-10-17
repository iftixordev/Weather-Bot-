import aiohttp
import logging
from config import WEATHER_API_KEY, WEATHER_API_URL, WEATHER_ICONS, WEATHER_TRANSLATIONS

logger = logging.getLogger(__name__)

class WeatherAPI:
    def __init__(self):
        self.api_key = WEATHER_API_KEY
        self.base_url = WEATHER_API_URL
    
    async def get_weather(self, city: str) -> dict:
        """Shahar uchun ob-havo ma'lumotlarini olish"""
        url = f"{self.base_url}/weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'en'  # O'zbek tili qo'llab-quvvatlanmaydi
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    logger.info(f"API so'rov: {url} - Status: {response.status}")
                    if response.status == 200:
                        data = await response.json()
                        logger.info(f"Muvaffaqiyatli javob: {city}")
                        return data
                    else:
                        error_text = await response.text()
                        logger.error(f"API xatolik {response.status}: {error_text}")
                        return None
        except Exception as e:
            logger.error(f"So'rov xatoligi: {e}")
            return None
    
    async def get_forecast(self, city: str) -> dict:
        """5 kunlik prognoz olish"""
        url = f"{self.base_url}/forecast"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'en'
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Forecast API xatolik {response.status}")
                        return None
        except Exception as e:
            logger.error(f"Forecast so'rov xatoligi: {e}")
            return None
    
    async def get_weather_by_coords(self, lat: float, lon: float) -> dict:
        """Koordinatalar bo'yicha ob-havo olish"""
        url = f"{self.base_url}/weather"
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'en'
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Coords API xatolik {response.status}")
                        return None
        except Exception as e:
            logger.error(f"Coords so'rov xatoligi: {e}")
            return None
    
    def format_weather(self, data: dict) -> str:
        """Ob-havo ma'lumotlarini formatlash"""
        if not data:
            return "❌ Ob-havo ma'lumotlari topilmadi"
        
        city = data['name']
        country = data['sys']['country']
        temp = round(data['main']['temp'])
        feels_like = round(data['main']['feels_like'])
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']
        wind_speed = data.get('wind', {}).get('speed', 0)
        
        # Icon va tarjima tanlash
        icon = WEATHER_ICONS.get(description.lower(), '🌡️')
        uz_description = WEATHER_TRANSLATIONS.get(description.lower(), description)
        
        return f"""
{icon} **{city}, {country}**

🌡️ **Harorat:** {temp}°C (his qilish: {feels_like}°C)
💧 **Namlik:** {humidity}%
🌬️ **Shamol:** {wind_speed} m/s
📊 **Bosim:** {pressure} hPa
📝 **Holat:** {uz_description.title()}
        """.strip()
    
    def format_forecast(self, data: dict) -> str:
        """5 kunlik prognozni formatlash"""
        if not data:
            return "❌ Prognoz ma'lumotlari topilmadi"
        
        city = data['city']['name']
        forecasts = []
        
        # Har kuni uchun bitta prognoz olish
        daily_forecasts = {}
        for item in data['list'][:15]:  # 5 kun x 3 vaqt = 15 ta
            date = item['dt_txt'].split()[0]
            if date not in daily_forecasts:
                daily_forecasts[date] = item
        
        result = f"📅 **5 kunlik prognoz - {city}**\n\n"
        
        for date, forecast in list(daily_forecasts.items())[:5]:
            temp = round(forecast['main']['temp'])
            description = forecast['weather'][0]['description']
            icon = WEATHER_ICONS.get(description.lower(), '🌡️')
            uz_description = WEATHER_TRANSLATIONS.get(description.lower(), description)
            
            result += f"{icon} **{date}:** {temp}°C - {uz_description.title()}\n"
        
        return result