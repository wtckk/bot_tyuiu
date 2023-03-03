from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_faq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('⁉ F.A.Q.'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)
