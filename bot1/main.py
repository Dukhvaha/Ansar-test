import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.book import router as book_router
from handlers.info_book import router as my_bookings_router

from db import createTable


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)
    dp.include_router(start_router)
    dp.include_router(book_router)
    dp.include_router(my_bookings_router)




    await dp.start_polling(bot)

if __name__ == '__main__':
    createTable()
    asyncio.run(main())