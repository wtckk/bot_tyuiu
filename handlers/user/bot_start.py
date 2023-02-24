from aiogram import types

from keyboards.default.keyboard_menu import kb_menu
from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer('Вы уже зарегистрированы.', reply_markup=kb_menu)
        elif user.status == 'banned':
            await message.answer('Вы заблокированы')
        await message.answer(f'Привет, {message.from_user.full_name}, я твой личный помощник! \n'
                         f'Обязательно попытаюсь тебе помочь.', reply_markup=kb_menu)
        await message.delete()
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active'
                                )
@dp.message_handler(text='⬅️ Назад в меню')
async def back_menu(message: types.Message):
    await message.answer(f'⬅️ Назад в меню', reply_markup=kb_menu)
    await message.delete()