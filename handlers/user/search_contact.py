from aiogram import types

from keyboards.default.keyboard_menu import kb_menu
from loader import dp


@dp.message_handler(text='☎️ Контакты')
async def search(message: types.Message):
    await message.answer(f'Введите ФИО преподователя')
