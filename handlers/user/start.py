from aiogram import types

from keyboards.default.keyboard_menu import kb_menu
from loader import dp


from filters import isPrivate

@dp.message_handler(isPrivate(), text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}, я твой личный помощник! \n'
                         f'Обязательно попытаюсь тебе помочь.', reply_markup=kb_menu)


@dp.message_handler(text='⬅️ Назад в меню')
async def back_menu(message: types.Message):
    await message.answer(f'⬅️ Назад в меню', reply_markup=kb_menu)
    await message.delete()