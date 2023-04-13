from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_profile = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('✍️ Ввод данных'),
            KeyboardButton('📃 Информация о себе')
        ],
        [
            KeyboardButton("⬅️ Назад в меню")
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)