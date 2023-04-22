from aiogram import executor
import settings
from handlers import dp
from db import database
import asyncio


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(database.init_db())

    executor.start_polling(dp, skip_updates=True)

