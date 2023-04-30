from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('👨‍🎓 Профиль')
        ],
        [
            KeyboardButton('🧭 Навигатор'),
            KeyboardButton('☎️ Контакты'),
            KeyboardButton("📅 Расписание")
        ],
        [
            KeyboardButton('📖 Справочник')
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)