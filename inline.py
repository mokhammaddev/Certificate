from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

one_line = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ortga", callback_data='menu'),
            InlineKeyboardButton(text="2-boshqichga o'tish", callback_data='two_line')
        ]
    ]
)


two_line = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='ortga', callback_data='one_line'),
            InlineKeyboardButton(text="3-bosqichga o'tish", callback_data='three_line')
        ]
    ]
)