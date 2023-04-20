from aiogram import executor
import settings
from handlers import dp


'''@dp.callback_query_handler(lambda c: c.data == 'continie')
async def click_continue(callback: types.CallbackQuery):
    message = await callback.message.answer(messages.page3_emoji)
    await asyncio.sleep(0.7)
    await message.delete()
    await asyncio.sleep(0.3)
    text = messages.page3_mes1[0]
    message = await callback.message.answer(text, parse_mode='HTML')
    for i in messages.page3_mes1[1:]:
        text += i
        if i:
            await asyncio.sleep(0.3)
            await message.edit_text(text, parse_mode='HTML')
            if i == 'Очередной бот с банальными видео, которые не досматривают до конца?\n':
                text = text.replace('Очередной', '<s>Очередной').replace('конца?', 'конца?</s>')
                await asyncio.sleep(0.3)
                await message.edit_text(text, parse_mode='HTML')'''
            


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

