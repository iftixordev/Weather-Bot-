from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from config import UZBEKISTAN_CITIES

def get_main_keyboard():
    """Asosiy klaviatura"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🌍 Shahar tanlash"), KeyboardButton(text="📍 Mening joylashuvim")],
            [KeyboardButton(text="🇺🇿 O'zbekiston shaharlari"), KeyboardButton(text="📊 5 kunlik prognoz")],
            [KeyboardButton(text="ℹ️ Yordam")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

def get_uzbekistan_cities_keyboard():
    """O'zbekiston shaharlari klaviaturasi"""
    buttons = []
    cities = list(UZBEKISTAN_CITIES.keys())
    
    # 2 tadan qilib joylash
    for i in range(0, len(cities), 2):
        row = []
        row.append(InlineKeyboardButton(text=cities[i], callback_data=f"city_{cities[i]}"))
        if i + 1 < len(cities):
            row.append(InlineKeyboardButton(text=cities[i + 1], callback_data=f"city_{cities[i + 1]}"))
        buttons.append(row)
    
    # Orqaga qaytish tugmasi
    buttons.append([InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_main")])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_weather_actions_keyboard(city: str):
    """Ob-havo harakatlari klaviaturasi"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔄 Yangilash", callback_data=f"refresh_{city}"),
                InlineKeyboardButton(text="📊 5 kunlik", callback_data=f"forecast_{city}")
            ],
            [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_cities")]
        ]
    )
    return keyboard

def get_location_keyboard():
    """Geolokatsiya klaviaturasi"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📍 Joylashuvni yuborish", request_location=True)],
            [KeyboardButton(text="🔙 Orqaga")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard