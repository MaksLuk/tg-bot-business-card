import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from loader import dp, bot
import settings
from db import database


with open('./handlers/message1/page1.txt', 'r', encoding='utf-8') as f:
    page_text = f.readlines()
page_text[0] += page_text.pop(1)


@dp.message_handler(commands=['start'])
async def start(message: types.Message, state: FSMContext):
    
    username = message.from_user.first_name
    text = page_text[0].replace('<ИМЯ>', username)
    mes = await message.answer(text)
    await asyncio.sleep(settings.dynamic_delay_many * len(text))
    for line in page_text[1:]:
        if line == 'Как тебе такая идея?:\n':
            text = text.replace('запарило:', 'запарило:<s>').replace('самому</b>', 'самому</b></s>')
            await mes.edit_text(text)
            await asyncio.sleep(settings.del_delay)
        text += line
        if line != '\n':
            await mes.edit_text(text)
            await asyncio.sleep(settings.dynamic_delay * len(line))
    button = InlineKeyboardMarkup().add(InlineKeyboardButton('ОТЛИЧНАЯ ИДЕЯ!', callback_data='continie'))
    await mes.edit_text(text, reply_markup=button)
    
    tg_username = message.from_user.username
    text = f'{username} @{tg_username} присоединился к боту!'
    
    insert = await database.insert_db(tg_username, 0)
    await state.update_data(times=0)
    if not insert:
        text += ' (повторно)'
        await state.update_data(times=1)
        
    new_joiner = await bot.send_message(chat_id=settings.admin_id, text=text)
    await state.update_data(message=new_joiner["message_id"])


