import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot, States
import emoji
from aiogram.dispatcher import FSMContext
import settings


@dp.callback_query_handler(lambda c: c.data == 'continue_to_7')
async def message_7(callback: types.CallbackQuery, state: FSMContext):
    await asyncio.sleep(settings.del_button_delay)
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)

    text = 'Высокие чеки, элементы воронки это хорошо, но ты спросишь как она будет приносить тебе деньги?\n\n'
    text += emoji.emojize(":red_triangle_pointed_down:") + ' Ответ в статье:\n<b>"Как игровая автоворонка будет приносить тебе деньги и сколько это стоит?"</b> ' + emoji.emojize(":orange_book:")
    button = InlineKeyboardMarkup().add(InlineKeyboardButton(emoji.emojize(":red_exclamation_mark:") + " Читать гайд " + emoji.emojize(":red_exclamation_mark:"), url=settings.guide2))
    await callback.message.answer(text, reply_markup=button)

    await asyncio.sleep(settings.guides_delay)
    await callback.message.answer(f'Напиши сюда {emoji.emojize(":backhand_index_pointing_down:")} ключевое слово, которое было в конце статьи, и мы продолжим...')
    await state.set_state(States.guide3)
    
