import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot, States
import emoji
from aiogram.dispatcher import FSMContext
from handlers.message3 import message_text
    

@dp.message_handler(state=States.guide1)
async def change_timer(message: types.Message, state: FSMContext):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    if message.text.strip().lower() != 'деньги':
        await message.answer('Поторопился, ввел неверно. Найди ключевое слово в конец статьи и попробуй еще раз')
        return
    await message.answer(message_text.text_question_1)
    await state.set_state(States.question1)


@dp.message_handler(state=States.question1)
async def change_timer(message: types.Message, state: FSMContext):
    if message.text.strip().lower().replace('.', '') != '3':
        await message.answer('Неверный ответ, перечитай статью и попробуй еще раз')
        return
    message = await message.answer(message_text.plus1)
    mes = await callback.message.answer(emoji.emojize(":money_with_wings:"))
    await asyncio.sleep(0.7)
    await mes.delete()
    await message.edit_text(message_text.plus1 + message_text.balance)
    button = InlineKeyboardMarkup().add(InlineKeyboardButton('ИСПЫТАТЬ УДАЧУ', callback_data='dice'))
    await message.answer(message_text.bowling, reply_markup=button)
    await state.reset_state()


@dp.callback_query_handler(lambda c: c.data == 'dice')
async def dice(callback: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)

    msg = await bot.send_dice(callback.from_user.id, emoji=emoji.emojize(":bowling:"))
    val = msg.dice.value
    if val < 3:
        val -= 1
    money_count = 1500 * val
    
    cegles = 'кегли' if val in [2, 3, 4] else 'кегль'
    text = f'Супер! ты сбил {html.escape("<")}{val}{html.escape(">")} {cegles} и заработал {html.escape("<")}+{money_count}{html.escape(">")} Монет\n\n'
    mes = await callback.message.answer(text)
    
    sleep(0.5)
    text += 'Шкала прогресса:\n' + emoji.emojize(":large_orange_diamond:") * 2 + emoji.emojize(":white_circle:") * 2
    await mes.edit_text(text)
    sleep(0.5)
    text += f'\n\nНа счету всего: {emoji.emojize(":dollar_banknote:")} {html.escape("<")}{3000 + money_count}{html.escape(">")} Монет'
