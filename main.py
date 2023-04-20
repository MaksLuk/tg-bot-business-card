from aiogram import executor
import settings
from handlers import dp


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

