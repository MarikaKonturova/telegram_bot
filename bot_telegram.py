from handlers import client, admin, other
from aiogram.utils import executor
from data_base import sqlite_db
from create_bot import dp


async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_client(dp)
other.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
