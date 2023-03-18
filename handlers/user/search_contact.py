from loader import dp

import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import markdown as md

from aiogram.types import CallbackQuery

from data.config import POSTGRES_URI as DATABASE_URL

from keyboards.inline import ikb_search


class FindTeacher(StatesGroup):
    waiting_for_teacher_name = State()


@dp.callback_query_handler(lambda c: c.data == 'repeat_search')
async def repeat_search(callback_query: CallbackQuery):
    await callback_query.answer("Введите ФИО преподавателя:")
    await FindTeacher.waiting_for_teacher_name.set()


@dp.callback_query_handler(lambda c: c.data == 'stop_search')
async def stop_search(callback_query: CallbackQuery):
    await callback_query.answer("Вы закончили поиск.")


async def find_teacher_start(message: types.Message):
    await message.answer("Введите ФИО преподавателя:")
    await FindTeacher.waiting_for_teacher_name.set()


async def find_teacher_process_name(message: types.Message, state: FSMContext):
    teacher_name = message.text.strip()

    async with asyncpg.create_pool(DATABASE_URL) as pool:
        async with pool.acquire() as con:
            teacher = await con.fetchrow("SELECT * FROM teachers WHERE name = $1", teacher_name)

    if teacher:
        teacher_info = md.text(
            md.text(f"{teacher['name']}"),
            md.text(f"Отдел: Кафедра {teacher['department']}"),
            md.text(f"Должность: {teacher['position']}"),
            md.text(f"Почта: {teacher['mail']}"),
            sep='\n'
        )
        await message.answer(teacher_info, parse_mode=ParseMode.MARKDOWN)
    else:
        await message.answer("Преподаватель не найден.", reply_markup=ikb_search)

    await state.finish()


dp.register_message_handler(find_teacher_start, text="☎️ Контакты")
dp.register_message_handler(
    find_teacher_process_name,
    state=FindTeacher.waiting_for_teacher_name,
    content_types=types.ContentTypes.TEXT
)
