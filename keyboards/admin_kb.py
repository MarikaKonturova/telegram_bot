from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')

button_case_admin = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)

button_case_admin.row(button_load, button_delete)
