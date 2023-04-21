import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from loader import dp, bot, States
import emoji
import settings


@dp.callback_query_handler(lambda c: c.data == 'continue_to_5')
async def message_5(callback: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    
    text = 'Высокий чек обсудили, теперь поймём что должно быть в мощной автоворонке, чтобы кратно увеличить доход!\n\n'
    mes = await callback.message.answer(text)
    await asyncio.sleep(settings.standart_delay)
    text += emoji.emojize(":red_triangle_pointed_down:") + ' <b>Читай статью "Элементы прибыльного наставничества"</b> и забирай <b>1500 Монет</b> + <b>ПОДАРОК</b> ' + emoji.emojize(":orange_book:")
    await asyncio.sleep(settings.standart_delay)
    await mes.edit_text(text)
    await asyncio.sleep(settings.standart_delay)
    await mes.edit_reply_markup(reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Читать', url='https://teletype.in/@smartchatbot/za6gUn6kpF2')))
    
    await asyncio.sleep(settings.guides_delay)
    await callback.message.answer('Напиши сюда ключевое слово, которое было в конце статьи и мы продолжим...')
    await state.set_state(States.guide2)

