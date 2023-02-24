from aiogram import types

from keyboards.default.keyboard_menu import kb_menu
from loader import dp


@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer(f'Команды не существует.')
