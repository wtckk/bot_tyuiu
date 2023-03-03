from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_navigation = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('⁉ F.A.Q.'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)
