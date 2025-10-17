from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, Location
from aiogram.filters import Command
from weather_api import WeatherAPI
from keyboards import (
    get_main_keyboard, 
    get_uzbekistan_cities_keyboard, 
    get_weather_actions_keyboard,
    get_location_keyboard
)
from config import UZBEKISTAN_CITIES

router = Router()
weather_api = WeatherAPI()

@router.message(Command("start"))
async def start_handler(message: Message):
    """Start komandasi"""
    welcome_text = """
🌤️ **Weather Bot'ga xush kelibsiz!**

Men sizga dunyoning istalgan joyidagi ob-havo haqida ma'lumot bera olaman.

🔹 Shahar nomini yozing
🔹 O'zbekiston shaharlarini tanlang  
🔹 Joylashuvingizni yuboring
🔹 5 kunlik prognoz oling

Boshlash uchun quyidagi tugmalardan foydalaning! 👇
    """
    await message.answer(welcome_text, reply_markup=get_main_keyboard(), parse_mode="Markdown")

@router.message(F.text == "ℹ️ Yordam")
async def help_handler(message: Message):
    """Yordam komandasi"""
    help_text = """
🆘 **Yordam**

**Qanday foydalanish:**
• Shahar nomini yozing (masalan: "Toshkent")
• "🇺🇿 O'zbekiston shaharlari" tugmasini bosing
• "📍 Mening joylashuvim" orqali geolokatsiya yuboring
• "📊 5 kunlik prognoz" tugmasini bosing

**Qo'llab-quvvatlanadigan tillar:**
• O'zbek, Ingliz, Rus va boshqa tillar

**Maslahat:** Shahar nomini ingliz tilida yozsangiz aniqroq natija olasiz.
    """
    await message.answer(help_text, parse_mode="Markdown")

@router.message(F.text == "🇺🇿 O'zbekiston shaharlari")
async def uzbekistan_cities_handler(message: Message):
    """O'zbekiston shaharlari"""
    await message.answer(
        "🇺🇿 **O'zbekiston shaharlarini tanlang:**", 
        reply_markup=get_uzbekistan_cities_keyboard(),
        parse_mode="Markdown"
    )

@router.message(F.text == "📍 Mening joylashuvim")
async def location_request_handler(message: Message):
    """Geolokatsiya so'rash"""
    await message.answer(
        "📍 **Joylashuvingizni yuboring**\n\nQuyidagi tugmani bosib, joylashuvingizni yuboring:",
        reply_markup=get_location_keyboard()
    )

@router.message(F.location)
async def location_handler(message: Message):
    """Geolokatsiya qabul qilish"""
    location: Location = message.location
    
    # Koordinatalar bo'yicha ob-havo olish
    weather_data = await weather_api.get_weather_by_coords(location.latitude, location.longitude)
    
    if weather_data:
        weather_text = weather_api.format_weather(weather_data)
        city_name = weather_data['name']
        await message.answer(
            weather_text, 
            reply_markup=get_weather_actions_keyboard(city_name),
            parse_mode="Markdown"
        )
    else:
        await message.answer("❌ Sizning joylashuvingiz uchun ob-havo ma'lumotlari topilmadi.")
    
    # Asosiy klaviaturaga qaytarish
    await message.answer("Boshqa amallar uchun:", reply_markup=get_main_keyboard())

@router.message(F.text == "🔙 Orqaga")
async def back_handler(message: Message):
    """Orqaga qaytish"""
    await message.answer("Asosiy menyu:", reply_markup=get_main_keyboard())

@router.callback_query(F.data.startswith("city_"))
async def city_callback_handler(callback: CallbackQuery):
    """Shahar tanlash callback"""
    city_uz = callback.data.replace("city_", "")
    city_en = UZBEKISTAN_CITIES.get(city_uz, city_uz)
    
    weather_data = await weather_api.get_weather(city_en)
    
    if weather_data:
        weather_text = weather_api.format_weather(weather_data)
        await callback.message.edit_text(
            weather_text,
            reply_markup=get_weather_actions_keyboard(city_en),
            parse_mode="Markdown"
        )
    else:
        await callback.answer("❌ Ob-havo ma'lumotlari topilmadi", show_alert=True)

@router.callback_query(F.data.startswith("refresh_"))
async def refresh_callback_handler(callback: CallbackQuery):
    """Ob-havoni yangilash"""
    city = callback.data.replace("refresh_", "")
    
    weather_data = await weather_api.get_weather(city)
    
    if weather_data:
        weather_text = weather_api.format_weather(weather_data)
        await callback.message.edit_text(
            weather_text,
            reply_markup=get_weather_actions_keyboard(city),
            parse_mode="Markdown"
        )
        await callback.answer("✅ Yangilandi!")
    else:
        await callback.answer("❌ Yangilashda xatolik", show_alert=True)

@router.callback_query(F.data.startswith("forecast_"))
async def forecast_callback_handler(callback: CallbackQuery):
    """5 kunlik prognoz"""
    city = callback.data.replace("forecast_", "")
    
    forecast_data = await weather_api.get_forecast(city)
    
    if forecast_data:
        forecast_text = weather_api.format_forecast(forecast_data)
        await callback.message.edit_text(
            forecast_text,
            reply_markup=get_weather_actions_keyboard(city),
            parse_mode="Markdown"
        )
    else:
        await callback.answer("❌ Prognoz ma'lumotlari topilmadi", show_alert=True)

@router.callback_query(F.data == "back_to_cities")
async def back_to_cities_handler(callback: CallbackQuery):
    """Shaharlar ro'yxatiga qaytish"""
    await callback.message.edit_text(
        "🇺🇿 **O'zbekiston shaharlarini tanlang:**",
        reply_markup=get_uzbekistan_cities_keyboard(),
        parse_mode="Markdown"
    )

@router.message()
async def city_search_handler(message: Message):
    """Shahar qidirish (matn orqali)"""
    city_name = message.text.strip()
    
    if len(city_name) < 2:
        await message.answer("❌ Shahar nomi juda qisqa. Kamida 2 ta harf kiriting.")
        return
    
    weather_data = await weather_api.get_weather(city_name)
    
    if weather_data:
        weather_text = weather_api.format_weather(weather_data)
        actual_city = weather_data['name']
        await message.answer(
            weather_text,
            reply_markup=get_weather_actions_keyboard(actual_city),
            parse_mode="Markdown"
        )
    else:
        await message.answer(
            f"❌ '{city_name}' shahri topilmadi.\n\n"
            "💡 **Maslahat:**\n"
            "• Shahar nomini to'g'ri yozing\n"
            "• Ingliz tilida yozing (Tashkent, Moscow)\n"
            "• O'zbekiston shaharlari uchun maxsus tugmani ishlating"
        )