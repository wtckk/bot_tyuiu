from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_search = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="🔁 Повторить поиск", callback_data="repeat_search"),
                                        InlineKeyboardButton(text="⏹️ Прекратить поиск", callback_data='stop_search')
                                    ],
                                ]
                                )