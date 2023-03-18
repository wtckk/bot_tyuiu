from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery
import asyncpg

from keyboards.default.keyboard_menu import kb_menu
from keyboards.default.keyboard_navigation import kb_navigation
from keyboards.inline import ikb_navigation

from data.config import POSTGRES_URI

from loader import dp, bot


@dp.message_handler(text='🧭 Навигатор')
async def command_navigation(message: types.Message):
    await message.answer("🧭 Навигатор", reply_markup=kb_navigation)
    await message.delete()


@dp.message_handler(text='🚪 Поиск аудитории')
async def command_audit(message: types.Message):
    await message.answer(f'Выберите нужный вам институт', reply_markup=ikb_navigation)



class BuildingNumber(StatesGroup):
    building = State()
    room = State()


@dp.callback_query_handler(lambda с: с.data in ['1', '2', '3', '4', '5', '6', '7'])
async def process_building_select(callback_query: CallbackQuery, state: FSMContext):
    building_number = int(callback_query.data)

    await bot.send_message(chat_id=callback_query.from_user.id, text="Введите номер кабинета")
    await BuildingNumber.room.set()
    await state.update_data(building_number=building_number)


@dp.message_handler(state=BuildingNumber.room)
async def proces_room_number(message: types.Message, state: FSMContext):
    try:
        room_number = int(message.text)
    except ValueError:
        await message.answer('Некорректный формат номера кабинета')
        return

    async with asyncpg.create_pool(POSTGRES_URI) as pool:
        async with pool.acquire() as conn:
            res = await conn.fetchrow("SELECT EXISTS(SELECT 1 FROM rooms WHERE building_number=$1 AND room_number=$2)",
                                (await state.get_data())['building_number'], room_number)

    if res[0]:
        floor = room_number // 100
        photo_path = f'navigation/{(await state.get_data())["building_number"]}/{floor}/{(await state.get_data())["building_number"]}_{room_number}.png'
        with open(photo_path, "rb") as photo:
            await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Кабинет не найден", reply_markup=kb_menu)

    await state.finish()

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
