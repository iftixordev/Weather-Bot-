import asyncio
import aiohttp
from config import WEATHER_API_KEY, WEATHER_API_URL

async def test_api():
    """API kalitini test qilish"""
    url = f"{WEATHER_API_URL}/weather"
    params = {
        'q': 'Tashkent',
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'en'
    }
    
    print(f"API URL: {url}")
    print(f"API Key: {WEATHER_API_KEY}")
    print(f"Params: {params}")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            print(f"Status: {response.status}")
            text = await response.text()
            print(f"Response: {text}")

if __name__ == "__main__":
    asyncio.run(test_api())