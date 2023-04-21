import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot
import emoji
import settings
from handlers.message2 import message_text


@dp.callback_query_handler(lambda c: c.data == 'continie')
async def click_continue(callback: types.CallbackQuery):
    await asyncio.sleep(settings.del_button_delay)
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    
    message = await callback.message.answer('⚡')
    await asyncio.sleep(settings.stiker_delay)
    await message.delete()
    await asyncio.sleep(settings.delay_between_stiker_and_message)

    text = message_text.text[0]
    mes = await callback.message.answer(text)
    await asyncio.sleep(settings.dynamic_delay_many * len(text))
    
    await mes.edit_text(text + message_text.text[1])
    await asyncio.sleep(settings.dynamic_delay * len(message_text.text[1]))
    text += message_text.text[2]
    await mes.edit_text(text)
    await asyncio.sleep(settings.del_delay)

    for i in message_text.text[3:]:
        text += i
        await mes.edit_text(text)
        delay = settings.dynamic_delay_many * len(i) if len(i) > 120 else settings.dynamic_delay * len(i)
        await asyncio.sleep(delay)
        
    button = InlineKeyboardMarkup().add(InlineKeyboardButton('ХОЧУ МОНЕТ', callback_data='get_money'))
    await mes.edit_reply_markup(reply_markup=button)


@dp.callback_query_handler(lambda c: c.data == 'get_money')
async def get_first_money(callback: types.CallbackQuery):
    await asyncio.sleep(settings.del_button_delay)
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    
    mes = await callback.message.answer(emoji.emojize(":money_with_wings:"))
    await asyncio.sleep(settings.money_stiker_delay)
    await mes.delete()
    
    text = message_text.end_text[0]
    mes = await callback.message.answer(text)
    await asyncio.sleep(settings.dynamic_delay * len(text))
    for i in message_text.end_text[1:]:
        text += i
        await mes.edit_text(text)
        await asyncio.sleep(settings.dynamic_delay * len(i))

    button = InlineKeyboardMarkup().add(InlineKeyboardButton('ПРОДОЛЖИТЬ', callback_data='continie2'))
    await mes.edit_reply_markup(reply_markup=button)

    
