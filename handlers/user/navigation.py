from aiogram import types

from keyboards.default.keyboard_menu import kb_menu
from keyboards.default.keyboard_navigation import kb_navigation
from keyboards.inline import ikb_navigation
from loader import dp


@dp.message_handler(text='🧭 Навигатор')
async def command_navigation(message: types.Message):
    await message.answer("🧭 Навигатор", reply_markup=kb_navigation)
    await message.delete()


@dp.message_handler(text='🚪 Поиск аудитории')
async def command_audit(message: types.Message):
    await message.answer(f'Выберите нужный вам институт', reply_markup=ikb_navigation)

@dp.message_handler(text='🌏 Расположение институтов')
async def command_legend(message: types.Message):
    await message.answer(
        f'Первый корпус - ул. Володарского, 38\n'
        f'Второй корпус - ул. Луначарского, 2\n'
        f'Третий корпус - ул. 50 лет Октября, 38\n'
        f'Четвертый корпус - ул. Володарского, 56\n'
        f'Пятый корпус - ул. Мельникайте, 72/1\n'
        f'Шестый корпус - ул. Луначарского, 2/6\n'
        f'Седьмой корпус - ул. Мельникайте, 70'
        )