import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from loader import dp, bot
import settings
from db import database


@dp.message_handler(lambda m: m.from_user.id == settings.admin_id)
async def admin_init(message: types.Message):
    buttons = [[types.KeyboardButton(text='Нажали "Старт"')],
               [types.KeyboardButton(text='Записались на разбор')],
               [types.KeyboardButton(text='Прошли до конца')],]
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer('Вы являетесь администратором.', reply_markup=keyboard)


@dp.message_handler(lambda m: m.text == 'Нажали "Старт"' and m.from_user.id == settings.admin_id)
async def stat1(message: types.Message):
    count, usernames = await database.get_statistics(0)
    messages = create_text(f'Начало работу с ботом: {count} человек\n', usernames)
    for mes in messages:
        await message.answer(mes)


@dp.message_handler(lambda m: m.text == 'Записались на разбор' and m.from_user.id == settings.admin_id)
async def stat3(message: types.Message):
    count, usernames = await database.get_statistics(1)
    messages = create_text(f'Записались на разбор: {count} человек\n', usernames)
    for mes in messages:
        await message.answer(mes)


@dp.message_handler(lambda m: m.text == 'Прошли до конца' and m.from_user.id == settings.admin_id)
async def stat3(message: types.Message):
    count, usernames = await database.get_statistics(2)
    messages = create_text(f'Прошли бота до конца: {count} человек\n', usernames)
    for mes in messages:
        await message.answer(mes)


@dp.message_handler()
async def every_message(message: types.Message):
    username = message.from_user.first_name
    tg_username = message.from_user.username
    await bot.send_message(chat_id=settings.admin_id, text=f'{username} @{tg_username} пишет вам:\n\n' + message.text)


def create_text(text, usernames):
    result = []
    for i in usernames:
        text += i + '\n'
        if len(text) > 4040:
            result.append(text)
            text = ''
    return result

