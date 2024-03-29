from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
import hashlib


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or "echo"
    link = "https://www.google.com/search?q=" + text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title="Статья Wikipedia: ",
        url=link,
        input_message_content=types.InputTextMessageContent(
            message_text=link))]

    await query.answer(articles, cache_time=1, is_personal=True)
executor.start_polling(dp, skip_updates=True)
