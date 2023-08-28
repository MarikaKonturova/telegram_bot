from aiogram import types, Dispatcher

import json
import string


# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation))
        for i in message.text.split(' ')}\
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(echo_send)
