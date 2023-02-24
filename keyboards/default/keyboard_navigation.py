from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_navigation = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('🚪 Поиск аудитории'),
            KeyboardButton('🌏 Расположение институтов')
        ],
        [
            KeyboardButton("⬅️ Назад в меню")
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)