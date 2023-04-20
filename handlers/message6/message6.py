import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot, States
import emoji
from aiogram.dispatcher import FSMContext
    

@dp.message_handler(state=States.guide2)
async def messaget_6(message: types.Message, state: FSMContext):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    
    if message.text.strip().lower() != 'автоворонка':
        await message.answer('Поторопился, ввел неверно. Найди ключевое слово в конец статьи и попробуй еще раз')
        return
    text = 'Ты справился с заданием. Добавляю + 1500 Монет\n\n'
    mes = await message.answer(text)

    emj = await message.answer(emoji.emojize(":money_with_wings:"))
    await asyncio.sleep(0.7)
    await emj.delete()

    text += 'Шкала прогресса:\n' + emoji.emojize(":large_orange_diamond:") * 3 + emoji.emojize(":white_circle:")
    await mes.edit_text(text)
    await asyncio.sleep(0.5)

    user_data = await state.get_data()
    new_balance = user_data["balance"] + 1500
    await state.update_data(balance=new_balance)
    text += f'\n\nНа счету всего: {emoji.emojize(":dollar_banknote:")} {html.escape("<")}{new_balance}{html.escape(">")} Монет'
    await mes.edit_text(text)
    await asyncio.sleep(0.5)
    text += f'\n\nДержи подарок от меня!'
    await mes.edit_text(text)
    await asyncio.sleep(0.5)

    # PDF

    button = InlineKeyboardMarkup().add(InlineKeyboardButton('Продолжаем', callback_data='continue_to_7'))
    await message.answer('А мы продолжаем. Осталось совсем чуть-чуть.', reply_markup=button)
    await state.set_state(None)

    
    
