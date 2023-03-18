from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_navigation = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                            InlineKeyboardButton(text='1️⃣', callback_data='1'),
                                            InlineKeyboardButton(text='2️⃣', callback_data='2'),
                                            InlineKeyboardButton(text='3️⃣', callback_data='3'),
                                            InlineKeyboardButton(text='4️⃣', callback_data='4'),

                                          ],
                                          [
                                              InlineKeyboardButton(text='5️⃣', callback_data='5'),
                                              InlineKeyboardButton(text='6️⃣', callback_data='6'),
                                              InlineKeyboardButton(text='7️⃣', callback_data="7"),
                                          ]
                                      ])