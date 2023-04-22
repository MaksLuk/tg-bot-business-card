import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from loader import dp, bot, States
import emoji
from aiogram.dispatcher import FSMContext
from handlers.message8 import message_text
import settings
from db import database
    

@dp.message_handler(state=States.guide3)
async def messaget_8(message: types.Message, state: FSMContext):
    if message.text.strip().lower() != settings.answer4:
        await message.answer('Поторопился, ввел неверно. Найди ключевое слово в конец статьи и попробуй еще раз')
        return
    text = f'Ты справился с заданием. \nДобавляю <b>+2000 Монет</b> {emoji.emojize(":flexed_biceps:")}\n\n'
    mes = await message.answer(text)
    await asyncio.sleep(settings.standart_delay)

    emj = await message.answer(emoji.emojize(":money_with_wings:"))
    await asyncio.sleep(settings.stiker_delay)
    await emj.delete()

    user_data = await state.get_data()
    new_balance = user_data["balance"] + 2000
    if new_balance > 15000:
        new_balance = 15000
    await state.update_data(balance=new_balance)
    text += f'Поздравляю! {emoji.emojize(":trophy:")} За всё время ты накопил {emoji.emojize(":dollar_banknote:")} <b>{new_balance} Монет</b>'
    await mes.edit_text(text)
    await asyncio.sleep(settings.standart_delay)

    text += '\n\nШкала прогресса: ' + settings.progress_emoji_1 * 4
    await mes.edit_text(text)
    await asyncio.sleep(settings.standart_delay)
    
    text += f'\n\nМонеты ты можешь потратить на создание игровой автоворонки!'
    await mes.edit_text(text)
    await asyncio.sleep(settings.standart_delay)

    await bot.send_audio(chat_id=message.from_user.id, audio=InputFile(settings.audio2))
    await asyncio.sleep(5)

    mess = message_text.text[0].split('\n')
    text = mess[0] + '\n'
    mes = await message.answer(text)
    await asyncio.sleep(settings.dynamic_delay * len(text))
    for i in mess[1:]:
        text += i + '\n'
        if i:
            await mes.edit_text(text)
            await asyncio.sleep(settings.dynamic_delay * len(i))

    for j in [1, 2]:
        for i in message_text.text[j].split('\n'):
            text += i + '\n'
            if i:
                await mes.edit_text(text)
                await asyncio.sleep(settings.dynamic_delay * len(i))
        
    button = InlineKeyboardMarkup().add(InlineKeyboardButton('Записаться на Разбор', callback_data='Go_go-go'))
    await mes.edit_reply_markup(reply_markup=button)

    await asyncio.sleep(2)
    await mes.pin()

    mes = await message.answer('Остались вопросы? Напиши мне в личку\n' + emoji.emojize(":backhand_index_pointing_right:") + ' @ottopk')
    await state.set_state(None)


@dp.callback_query_handler(lambda c: c.data == 'Go_go-go')
async def gooooo(callback: types.CallbackQuery, state: FSMContext):
    await asyncio.sleep(settings.del_button_delay)
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    
    text = 'Супер! Записал тебя на Разбор ' + emoji.emojize(":check_mark_button:") + '\n\nЧтобы сэкономить нам время на разборе и дать еще больше пользы – ответь на 3 простых вопроса ' + emoji.emojize(":backhand_index_pointing_down:")
    await callback.message.answer(text)

    await asyncio.sleep(1)
    await callback.message.answer('<b>1/3. Какой у тебя оффер / что продаешь?</b>')
    await state.set_state(States.main_question1)

    tg_username = callback.from_user.username
    user_data = await state.get_data()
    await bot.delete_message(chat_id=callback.from_user.id, message_id=user_data["message"])
    text=f'{callback.from_user.first_name} @{tg_username}\nБаллов: {user_data["balance"]}\nЗаписался на разбор: {emoji.emojize(":check_mark:")}'

    await database.insert_db(tg_username, 1)
    if user_data['times']:
        text += ' (повторно)'

    new_joiner = await bot.send_message(chat_id=settings.admin_id, text=text)
    await state.update_data(message=new_joiner["message_id"])
    
    
@dp.message_handler(state=States.main_question1)
async def question1(message: types.Message, state: FSMContext):
    await state.update_data(answer1=message.text)
    await message.answer('<b>2/3. С каким чеком сейчас продаешь?</b>')
    await state.set_state(States.main_question2)


@dp.message_handler(state=States.main_question2)
async def question2(message: types.Message, state: FSMContext):
    await state.update_data(answer2=message.text)
    await message.answer('<b>3/3. На какой доход в месяц хочешь выйти?</b>')
    await state.set_state(States.main_question3)


@dp.message_handler(state=States.main_question3)
async def question3(message: types.Message, state: FSMContext):
    await asyncio.sleep(4)
    await bot.send_audio(chat_id=message.from_user.id, audio=InputFile(settings.audio3))

    tg_username = message.from_user.username
    user_data = await state.get_data()
    await bot.delete_message(chat_id=message.from_user.id, message_id=user_data["message"])

    text = f'{message.from_user.first_name} @{tg_username}' \
                           f'\nБаллов: {user_data["balance"]}' \
                           f'\nЗаписался на разбор: {emoji.emojize(":check_mark:")}\n' \
                           f'Ответы на вопросы:\n' \
                           f'1. {user_data["answer1"]}\n' \
                           f'2. {user_data["answer2"]}\n' \
                           f'3. {message.text}\n'

    await database.insert_db(tg_username, 2)
    if user_data['times']:
        text = 'Повторно:\n' + text

    await bot.send_message(chat_id=settings.admin_id, text=text)
    await state.finish()

