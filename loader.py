from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import settings


class States(StatesGroup):
    guide1: State = State()
    question1: State = State()
    guide2: State = State()
    guide3: State = State()
    main_question1: State = State()
    main_question2: State = State()
    main_question3: State = State()


storage = MemoryStorage()
bot = Bot(settings.bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)



