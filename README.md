# 🌤️ Weather Bot

Zamonaviy Telegram Weather Bot - dunyoning istalgan joyidagi ob-havo ma'lumotlarini olish uchun.

## ✨ Xususiyatlar

- 🌍 **Global ob-havo**: Dunyoning istalgan shahri
- 🇺🇿 **O'zbekiston shaharlari**: Maxsus klaviatura
- 📍 **Geolokatsiya**: Joylashuvingiz bo'yicha ob-havo
- 📊 **5 kunlik prognoz**: Kelajakdagi ob-havo
- 🔄 **Real-time yangilanish**: Darhol yangi ma'lumotlar
- 🎨 **Zamonaviy interfeys**: Qulay klaviaturalar va emoji

## 🚀 O'rnatish

### 1. Repository'ni clone qiling
```bash
git clone https://github.com/yourusername/weather-bot.git
cd weather-bot
```

### 2. Virtual environment yarating
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki
venv\\Scripts\\activate  # Windows
```

### 3. Kerakli kutubxonalarni o'rnating
```bash
pip install -r requirements.txt
```

### 4. Environment o'zgaruvchilarini sozlang
```bash
cp .env.example .env
```

`.env` faylini tahrirlang:
```env
BOT_TOKEN=your_telegram_bot_token_here
WEATHER_API_KEY=your_openweathermap_api_key_here
```

### 5. API kalitlarini oling

#### Telegram Bot Token:
1. [@BotFather](https://t.me/BotFather) ga boring
2. `/newbot` komandasi yuboring
3. Bot nomini va username'ini kiriting
4. Olingan tokenni `.env` fayliga qo'ying

#### OpenWeatherMap API Key:
1. [OpenWeatherMap](https://openweathermap.org/api) saytiga ro'yxatdan o'ting
2. API key oling (bepul)
3. Kalitni `.env` fayliga qo'ying

### 6. Botni ishga tushiring
```bash
python main.py
```

## 📱 Qanday foydalanish

### Asosiy komandalar:
- `/start` - Botni boshlash
- Shahar nomini yozing (masalan: "Toshkent", "Moscow")
- "🇺🇿 O'zbekiston shaharlari" tugmasini bosing
- "📍 Mening joylashuvim" orqali geolokatsiya yuboring

### Qo'llab-quvvatlanadigan shaharlar:
- **O'zbekiston**: Toshkent, Samarqand, Buxoro, Andijon va boshqalar
- **Dunyo**: London, New York, Tokyo, Paris va 200,000+ shahar

## 🏗️ Loyiha strukturasi

```
weather-bot/
├── main.py              # Asosiy fayl
├── config.py            # Konfiguratsiya
├── weather_api.py       # Weather API handler
├── keyboards.py         # Telegram klaviaturalar
├── handlers.py          # Message va callback handlers
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # Dokumentatsiya
```

## 🛠️ Texnologiyalar

- **aiogram 3.3.0** - Telegram Bot API
- **aiohttp** - Async HTTP client
- **OpenWeatherMap API** - Ob-havo ma'lumotlari
- **python-dotenv** - Environment variables

## 📊 API Ma'lumotlari

Bot quyidagi ma'lumotlarni taqdim etadi:
- 🌡️ Harorat (haqiqiy va his qilinadigan)
- 💧 Namlik foizi
- 🌬️ Shamol tezligi
- 📊 Atmosfera bosimi
- 📝 Ob-havo holati
- 📅 5 kunlik prognoz

## 🔧 Sozlash

### O'zbekiston shaharlarini qo'shish:
`config.py` faylida `UZBEKISTAN_CITIES` lug'atiga yangi shaharlar qo'shing:

```python
UZBEKISTAN_CITIES = {
    'Yangi Shahar': 'New City',
    # ...
}
```

### Yangi emoji qo'shish:
`config.py` faylida `WEATHER_ICONS` lug'atini yangilang:

```python
WEATHER_ICONS = {
    'new weather': '🆕',
    # ...
}
```

## 🚀 Deploy qilish

### Heroku:
1. Heroku account yarating
2. `Procfile` yarating: `web: python main.py`
3. Environment variables sozlang
4. Deploy qiling

### VPS:
1. Serverni sozlang
2. PM2 yoki systemd ishlatib xizmat yarating
3. Nginx reverse proxy sozlang (ixtiyoriy)

## 🤝 Hissa qo'shish

1. Fork qiling
2. Feature branch yarating (`git checkout -b feature/AmazingFeature`)
3. Commit qiling (`git commit -m 'Add some AmazingFeature'`)
4. Push qiling (`git push origin feature/AmazingFeature`)
5. Pull Request oching

## 📄 Litsenziya

Bu loyiha MIT litsenziyasi ostida tarqatiladi. Batafsil ma'lumot uchun `LICENSE` faylini ko'ring.

## 📞 Aloqa

- **Telegram**: [@yourusername](https://t.me/Iftixorme)
- **Email**: iftixortoychiyev@gmail.com
- **GitHub**: [yourusername](https://github.com/Iftixordev)

## 🙏 Minnatdorchilik

- [OpenWeatherMap](https://openweathermap.org/) - Ob-havo API
- [aiogram](https://github.com/aiogram/aiogram) - Telegram Bot framework
- [Telegram](https://telegram.org/) - Messaging platform

---

⭐ Agar loyiha yoqsa, star bosishni unutmang!# Weather-Bot-
