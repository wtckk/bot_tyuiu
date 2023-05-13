from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_role = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(text="👨‍🎓 Студент", callback_data='student'),
                        InlineKeyboardButton(text="👨‍🏫 Преподаватель", callback_data='teacher')
                    ]
                ]
            )