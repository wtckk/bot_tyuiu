from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_navigation = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                            InlineKeyboardButton(text='1️⃣', callback_data='search'),
                                            InlineKeyboardButton(text='2️⃣', callback_data='search'),
                                            InlineKeyboardButton(text='3️⃣', callback_data='search'),
                                            InlineKeyboardButton(text='4️⃣', callback_data='search'),

                                          ],
                                          [
                                              InlineKeyboardButton(text='5️⃣', callback_data='search'),
                                              InlineKeyboardButton(text='6️⃣', callback_data='search'),
                                              InlineKeyboardButton(text='7️⃣', callback_data="search"),
                                          ]
                                      ])