from aiogram import Bot, Dispatcher, types
import settings

bot = Bot(settings.bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot) # storage=storage


#from aiogram.dispatcher import FSMContext
#from aiogram.dispatcher.filters.state import StatesGroup, State
#from aiogram.contrib.fsm_storage.memory import MemoryStorage

#storage = MemoryStorage()
