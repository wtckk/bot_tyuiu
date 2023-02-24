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
    await message.answer(f'УЛК-01 — г. Тюмень, ул. Володарского, 38\n'
        f'УЛК-01А — ул. Орджоникидзе, 54\n'
        f'УЛК-02 — ул. Мельникайте, 72\n'
        f'УЛК-03 — ул. 50 лет Октября, 38\n'
        f'УК-07 — ул. Мельникайте, 70\n'
        f'УЛК-04 — ул. Володарского, 56\n'
        f'ИЛК-09 — ул. Луначарского, 4\n'
        f'УЛК-08 — ул. Луначарского, 2\n'
        f'УК-08/2 — ул. Луначарского, 2, корпус 2\n'
        f'ИЛК-08/1 — ул. Луначарского, 2, корпус 1\n'
        f'УК-08/3 — ул. Луначарского, 2, корпус 3\n'
        f'УК-08/4 — ул. Луначарского, 2, корпус 4\n'
        f'ИЛК-08/6 — ул. Луначарского, 2, корпус 6\n'
        f'ИЛК-11 — ул. Энергетиков, 44\n'
        f'УК-10 — ул. Энергетиков, 44, корпус 1\n'
        f'БИК — ул. Мельникайте, 72\n'
                         )