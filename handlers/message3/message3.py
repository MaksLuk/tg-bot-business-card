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
    await asyncio.sleep(settings.del_button_delay)
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)

    message = await callback.message.answer(message_text.text)
    await asyncio.sleep(settings.dynamic_delay_many * len(message_text.text))
    
    await message.edit_text(message_text.text + message_text.end)
    await asyncio.sleep(settings.dynamic_delay * len(message_text.end))
    
    button = InlineKeyboardMarkup().add(InlineKeyboardButton(emoji.emojize(":red_exclamation_mark:") + " Читать гайд " + emoji.emojize(":red_exclamation_mark:"), url=settings.guide1))
    await message.edit_reply_markup(reply_markup=button)
    
    await asyncio.sleep(settings.guides_delay)
    await message.answer(message_text.text_question_1)
    await state.set_state(States.question1)
    
