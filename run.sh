#!/bin/bash

# Weather Bot ishga tushirish skripti

echo "🌤️ Weather Bot ishga tushirilmoqda..."

# Virtual environment tekshirish
if [ ! -d "venv" ]; then
    echo "Virtual environment yaratilmoqda..."
    python3 -m venv venv
fi

# Virtual environment faollashtirish
source venv/bin/activate

# Dependencies o'rnatish
echo "Dependencies o'rnatilmoqda..."
pip install -r requirements.txt

# .env fayl tekshirish
if [ ! -f ".env" ]; then
    echo "❌ .env fayl topilmadi!"
    echo "📝 .env.example faylini .env ga nusxalang va API kalitlarini kiriting."
    exit 1
fi

# Botni ishga tushirish
echo "🚀 Bot ishga tushirilmoqda..."
python main.py