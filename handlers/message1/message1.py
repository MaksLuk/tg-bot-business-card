import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp


with open('./handlers/message1/page1.txt', 'r', encoding='utf-8') as f:
    page_text = f.readlines()
page_text[0] += page_text.pop(1)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    username = message.from_user.first_name
    text = page_text[0].replace('<ИМЯ>', username)
    message = await message.answer(text)
    for line in page_text[1:]:
        if line == 'Как тебе такая идея?:\n':
            text = text.replace('запарило:', 'запарило:<s>').replace('самому</b>', 'самому</b></s>')
        text += line
        if line != '\n':
            await asyncio.sleep(0.3)
            await message.edit_text(text)
    button = InlineKeyboardMarkup().add(InlineKeyboardButton('ОТЛИЧНАЯ ИДЕЯ!', callback_data='continie'))
    await message.edit_text(text, reply_markup=button)
