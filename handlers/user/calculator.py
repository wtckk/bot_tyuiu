from aiogram import types
from keyboards.default.keyboard_menu import kb_menu
from loader import dp

@dp.message_handler(text='📖 Калькулятор ЕГЭ')
async def calculator(message: types.Message):
    pass