import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot, States
import emoji
from aiogram.dispatcher import FSMContext
import settings


@dp.callback_query_handler(lambda c: c.data == 'continue_to_7')
async def message_7(callback: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)

    text = 'Высокие чеки, элементы воронки это хорошо, но ты спросишь как она будет приносить тебе деньги?\n\n'
    mes = await callback.message.answer(text)
    await asyncio.sleep(settings.standart_delay)
    text += emoji.emojize(":red_triangle_pointed_down:") + ' Ответ в статье:\n<b>"Как игровая автоворонка будет приносить тебе деньги и сколько это стоит?"</b> ' + emoji.emojize(":orange_book:")
    await asyncio.sleep(settings.standart_delay)
    await mes.edit_text(text)
    await asyncio.sleep(settings.standart_delay)
    await mes.edit_reply_markup(reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Читать', url='https://teletype.in/@smartchatbot/cStvUsIyl8O')))

    await asyncio.sleep(settings.guides_delay)
    await callback.message.answer('Напиши сюда ключевое слово, которое было в конце статьи')
    await state.set_state(States.guide3)
    
