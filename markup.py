from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


bosh_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Boshlash💥')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)
