import asyncio
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp


with open('./handlers/message2/page2.txt', 'r', encoding='utf-8') as f:
    page_text = f.readlines()

with open('./handlers/message2/page2_emodjies.txt', 'r', encoding='utf-8') as f:
    emodjies = f.read().split('\n_______________')


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
            await asyncio.sleep(0.7)
            await message.edit_text(text)
            if i == 'Очередной бот с банальными видео, которые не досматривают до конца?\n':
                text = text.replace('Очередной', '<s>Очередной').replace('конца?', 'конца?</s>')
                await asyncio.sleep(0.7)
                await message.edit_text(text)
    # дальше должны падать монеты
    text += '\n'
    for emoji in emodjies:
        await message.edit_text(text + emoji)
        await asyncio.sleep(0.1)
    text += emodjies[-1]
    
