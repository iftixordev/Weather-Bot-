import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import BOT_TOKEN
from handlers import router

# Logging sozlash
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Asosiy funksiya"""
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN topilmadi! .env faylini tekshiring.")
        return
    
    # Bot va Dispatcher yaratish
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )
    
    dp = Dispatcher()
    dp.include_router(router)
    
    logger.info("🌤️ Weather Bot ishga tushmoqda...")
    
    try:
        # Bot ma'lumotlarini olish
        bot_info = await bot.get_me()
        logger.info(f"Bot nomi: {bot_info.first_name} (@{bot_info.username})")
        
        # Polling boshlash
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Xatolik yuz berdi: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot to'xtatildi.")