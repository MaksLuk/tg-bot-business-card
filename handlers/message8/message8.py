import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot, States
import emoji
from aiogram.dispatcher import FSMContext
from handlers.message8 import message_text
    

@dp.message_handler(state=States.guide3)
async def messaget_8(message: types.Message, state: FSMContext):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    
    if message.text.strip().lower() != 'масштаб':
        await message.answer('Поторопился, ввел неверно. Найди ключевое слово в конец статьи и попробуй еще раз')
        return
    text = 'Ты справился с заданием. Добавляю + 2000 Монет\n\n'
    mes = await message.answer(text)

    emj = await message.answer(emoji.emojize(":money_with_wings:"))
    await asyncio.sleep(0.7)
    await emj.delete()

    text += 'Шкала прогресса:\n' + emoji.emojize(":large_orange_diamond:") * 4
    await mes.edit_text(text)
    await asyncio.sleep(0.5)

    user_data = await state.get_data()
    new_balance = user_data["balance"] + 2000
    await state.update_data(balance=new_balance)
    text += f'\n\nНа счету всего: {emoji.emojize(":dollar_banknote:")} {html.escape("<")}{new_balance}{html.escape(">")} Монет'
    await mes.edit_text(text)
    await asyncio.sleep(0.5)
    text += f'\n\nМонеты ты можешь потратить на создание игровой автоворонки!'
    await mes.edit_text(text)
    await asyncio.sleep(0.5)

    # аудио 2

    mes = message_text.offer_text.split('\n')
    text = mes[0] + '\n
    mes = await message.answer(text)
    for i in mes[1:]:
        text += i + '\n'
        if i:
            await asyncio.sleep(0.5)
            await mes.edit_text(text)
    sleep(0.5)
    button = InlineKeyboardMarkup().add(InlineKeyboardButton('Записаться на Разбор', callback_data='Go_go-go'))
    await mes.edit_reply_markup(reply_markup=button)
    await mes.pin()

    await asyncio.sleep(2)

    mes = message_text.bonuses.split('\n')
    text = mes[0] + '\n
    mes = await message.answer(text)
    for i in mes[1:]:
        text += i + '\n'
        if i:
            await asyncio.sleep(0.5)
            await mes.edit_text(text)

    await state.set_state(None)


@dp.callback_query_handler(lambda c: c.data == 'Go_go-go')
async def gooooo(callback: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    text = 'Супер! Записал тебя Разбор ' + emoji.emojize(":check_mark_button:") + '\n\nЧтобы сэкономить нам время на разборе и дать еще больше пользы – ответь на 3 простых вопроса ' + emoji.emojize(":backhand_index_pointing_down:")
    await callback.message.answer(text)

    await asyncio.sleep(1)
    await callback.message.answer('<b>1/3. Какой у тебя оффер / что продаешь?</b>')
    await state.set_state(States.main_question1)
    
    
@dp.message_handler(state=States.main_question1)
async def question1(message: types.Message, state: FSMContext):
    await message.answer('<b>2/3. С каким чеком сейчас продаешь?</b>')
    await state.set_state(States.main_question2)

@dp.message_handler(state=States.main_question1)
async def question2(message: types.Message, state: FSMContext):
    await message.answer('<b>2/3. С каким чеком сейчас продаешь?</b>')
    await state.set_state(States.main_question2)

@dp.message_handler(state=States.main_question1)
async def question3(message: types.Message, state: FSMContext):
    # АУДИО
    pass

