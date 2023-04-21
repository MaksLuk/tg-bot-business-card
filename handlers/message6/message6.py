import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from loader import dp, bot, States
import emoji
from aiogram.dispatcher import FSMContext
import settings
    

@dp.message_handler(state=States.guide2)
async def messaget_6(message: types.Message, state: FSMContext):
    if message.text.strip().lower() != settings.answer3:
        await message.answer('Поторопился, ввел неверно. Найди ключевое слово в конец статьи и попробуй еще раз')
        return
    text = 'Ты справился с заданием' + emoji.emojize(":party_popper:") + emoji.emojize(":confetti_ball:") + '\nДобавляю <b>+1500 Монет</b>'
    mes = await message.answer(text)
    await asyncio.sleep(settings.standart_delay)

    emj = await message.answer(emoji.emojize(":money_with_wings:"))
    await asyncio.sleep(settings.stiker_delay)
    await emj.delete()

    user_data = await state.get_data()
    new_balance = user_data["balance"] + 1500
    await state.update_data(balance=new_balance)
    text += f'\n\nНа счету всего: {emoji.emojize(":dollar_banknote:")} <b>{new_balance} Монет</b>'
    await mes.edit_text(text)
    await asyncio.sleep(settings.standart_delay)

    text += '\n\nШкала прогресса: ' + settings.progress_emoji_1 * 3 + settings.progress_emoji_2
    await mes.edit_text(text)
    await asyncio.sleep(settings.standart_delay)

    await message.answer('Держи подарок от меня! ' + emoji.emojize(":ledger:"))
    await asyncio.sleep(0.3)

    await bot.send_document(chat_id=message.from_user.id, document=InputFile(settings.pdf))
    
    await asyncio.sleep(1)

    button = InlineKeyboardMarkup().add(InlineKeyboardButton('Продолжаем', callback_data='continue_to_7'))
    await message.answer(f'А мы продолжаем {emoji.emojize(":backhand_index_pointing_right:")} Осталось совсем чуть-чуть.', reply_markup=button)
    await state.set_state(None)

    
    
