from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("start"))
async def menu(message: types.Message):
    pass