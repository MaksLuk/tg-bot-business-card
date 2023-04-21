import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot, States
import emoji
import html
from aiogram.dispatcher import FSMContext
from handlers.message3 import message_text
import settings


@dp.callback_query_handler(lambda c: c.data == 'continie2')
async def click_continue2(callback: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)

    raw_text = message_text.text.split('\n')
    text = raw_text[0] + '\n'
    message = await callback.message.answer(text)
    for i in raw_text[1:]:
        text += i + '\n'
        if i:
            await asyncio.sleep(settings.standart_delay)
            await message.edit_text(text)
    
    button = InlineKeyboardMarkup().add(InlineKeyboardButton('Читать гайд "Продажи на высокий чек"!', url='https://teletype.in/@ottopk/fSCpmr2DKpf'))
    await message.edit_text(text, reply_markup=button)
    await asyncio.sleep(settings.guides_delay)
    await callback.message.answer('Напиши сюда ключевое слово, которое было в конце статьи, и мы продолжим...')
    await state.set_state(States.guide1)
    
