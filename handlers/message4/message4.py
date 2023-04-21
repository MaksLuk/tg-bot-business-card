import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from loader import dp, bot, States
import emoji
from aiogram.dispatcher import FSMContext
from handlers.message4 import message_text
import settings
    

@dp.message_handler(state=States.guide1)
async def get_keyword_first(message: types.Message, state: FSMContext):
    if message.text.strip().lower() != settings.answer1:
        await message.answer('Поторопился, ввел неверно. Найди ключевое слово в конец статьи и попробуй еще раз')
        return

    await message.answer(message_text.text_question_1)
    await state.set_state(States.question1)


@dp.message_handler(state=States.question1)
async def get_question_first(message: types.Message, state: FSMContext):
    if not message.text.strip().lower().replace('.', '') in settings.answer2:
        await message.answer('Неверный ответ, перечитай статью и попробуй еще раз')
        return

    emj = await message.answer(emoji.emojize(":party_popper:"))
    await asyncio.sleep(settings.stiker_delay)
    await emj.delete()
    
    mes = await message.answer(message_text.plus1)
    await asyncio.sleep(settings.dynamic_delay * len(message_text.plus1))
    emj = await message.answer(emoji.emojize(":money_with_wings:"))
    await asyncio.sleep(settings.stiker_delay)
    await emj.delete()
    await mes.edit_text(message_text.plus1 + message_text.balance)

    await asyncio.sleep(0.5)
    await bot.send_audio(chat_id=message.from_user.id, audio=InputFile(settings.audio1))
    await asyncio.sleep(5)
    
    button = InlineKeyboardMarkup().add(InlineKeyboardButton('ИСПЫТАТЬ УДАЧУ', callback_data='dice'))
    await message.answer(message_text.bowling, reply_markup=button)
    await state.set_state(None)


@dp.callback_query_handler(lambda c: c.data == 'dice')
async def dice(callback: types.CallbackQuery, state: FSMContext):
    msg = await bot.send_dice(callback.from_user.id, emoji=emoji.emojize(":bowling:"))
    
    await asyncio.sleep(settings.del_button_delay)
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    
    val = msg.dice.value
    if val < 3:
        val -= 1
    money_count = 1500 * val

    await asyncio.sleep(settings.dice_delay - settings.del_button_delay)
    
    cegles = 'кегли' if val in [2, 3, 4] else 'кеглю' if val == 1 else 'кегль'
    text = f'Супер! ты сбил <b>{val}</b> {cegles} и заработал <b>+{money_count}</b> Монет'
    mes = await callback.message.answer(text)

    emj = await callback.message.answer(emoji.emojize(":money_with_wings:"))
    await asyncio.sleep(settings.stiker_delay)
    await emj.delete()

    text += f'\n\nНа счету всего: {emoji.emojize(":dollar_banknote:")} <b>{3000 + money_count} Монет</b>'
    await mes.edit_text(text)
    await asyncio.sleep(settings.standart_delay)
    
    text += '\nШкала прогресса: ' + settings.progress_emoji_1 * 2 + settings.progress_emoji_2 * 2
    await mes.edit_text(text)
    await asyncio.sleep(settings.standart_delay)
    
    text += f'\n\n<b>Продолжаем?</b> ' + emoji.emojize(":raising_hands:")
    await mes.edit_reply_markup(reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Продолжить', callback_data='continue_to_5')))

    await state.update_data(balance=3000+money_count)
    
