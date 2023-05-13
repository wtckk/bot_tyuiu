from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_schedule = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text="⬅️", callback_data="prev_day"),
                                            InlineKeyboardButton(text="➡️", callback_data="next_day")
                                        ]
                                    ]
                                    )

