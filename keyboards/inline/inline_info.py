from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_info = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="Educon", callback_data="educon"),
                                        InlineKeyboardButton(text="Modeus", callback_data="modeus")

                                    ],
                                    [
                                        InlineKeyboardButton(text="Библиотека ТИУ", callback_data='library')
                                    ],
                                ]
                                )


