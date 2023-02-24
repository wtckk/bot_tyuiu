from aiogram import types

from keyboards.default.keyboard_menu import kb_menu
from loader import dp


@dp.message_handler(text='📌 Информация о боте')
async def buttons(message: types.Message):
    await message.answer(f'Бот создан для')
