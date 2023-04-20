import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
import emoji
import html


with open('./handlers/message2/page2.txt', 'r', encoding='utf-8') as f:
    page_text = f.readlines()


end_text = [f'На счету: {emoji.emojize(":dollar_banknote:")} {html.escape("<")}1000{html.escape(">")} Монет\n\n',
            f'А теперь расскажу как "намайнить" реальные деньги {emoji.emojize(":money_bag:")*2}']
    

@dp.callback_query_handler(lambda c: c.data == 'continie')
async def click_continue(callback: types.CallbackQuery):
    message = await callback.message.answer('⚡')
    await asyncio.sleep(0.7)
    await message.delete()
    await asyncio.sleep(0.3)
    text = page_text[0]
    message = await callback.message.answer(text)
    for i in page_text[1:]:
        text += i
        if i != '\n':
            await asyncio.sleep(0.5)
            await message.edit_text(text)
            if i == 'Очередной бот с банальными видео, которые не досматривают до конца?\n':
                text = text.replace('Очередной', '<s>Очередной').replace('конца?', 'конца?</s>')
                await asyncio.sleep(0.5)
                await message.edit_text(text)
    # дальше должны падать монеты
    text += '\n'
    mes = await callback.message.answer(emoji.emojize(":money_with_wings:"))
    await asyncio.sleep(0.7)
    await mes.delete()
    for i in range(0, 10, 2):
        await message.edit_text(text + emoji.emojize(":money_with_wings:")*i + emoji.emojize(":white_circle:")*(8-i))
        await asyncio.sleep(0.3)
    text += emoji.emojize(":money_with_wings:")*8 + '\n\n'
    for i in end_text:
        text += i
        await asyncio.sleep(0.5)
        await message.edit_text(text)
    await asyncio.sleep(0.5)
    button = InlineKeyboardMarkup().add(InlineKeyboardButton('ПРОДОЛЖИТЬ!', callback_data='continie2'))
    await message.edit_text(text, reply_markup=button)

    
