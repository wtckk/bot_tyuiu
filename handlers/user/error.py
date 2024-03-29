from aiogram import types

from keyboards.default.keyboard_menu import kb_menu
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=3)
@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer(f'Команды не существует', reply_markup=kb_menu)
