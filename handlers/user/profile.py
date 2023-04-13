import asyncpg

from keyboards.default import kb_profile
from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from data.config import POSTGRES_URI
from utils.parser_educon import valid


@dp.message_handler(text='👨‍🎓 Профиль')
async def profile(message: types.Message):
    await message.answer("👨‍🎓 Профиль", reply_markup=kb_profile)
    await message.delete()


@dp.message_handler(text='📃 Информация о себе')
async def info_user(message: types.Message):
    user_id = message.from_user.id
    async with asyncpg.create_pool(POSTGRES_URI) as pool:
        async with pool.acquire() as conn:
            result = await conn.fetchrow('select login, password FROM user_auth WHERE user_id=$1', user_id)
    login = result['login'] if result else '⬜️'
    password = result['password'] if result else '⬜️'
    await message.answer(f"Ваш user_id: {user_id}\nВаш логин: {login}\nВаш пароль: {password}")
class LoginState(StatesGroup):
    waiting_login = State()
    waiting_password = State()

@dp.message_handler(text='✍️ Ввод данных')
async def cmd_login(message: types.Message):
    await message.answer("Введите логин для систем Modeus и Educon")
    await LoginState.waiting_login.set()


@dp.message_handler(state=LoginState.waiting_login)
async def process_login(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text

    await message.answer("Введите пароль")
    await LoginState.waiting_password.set()


@dp.message_handler(state=LoginState.waiting_password)
async def process_password(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
        data['user_id'] = message.from_user.id
        if valid(data['login'], data['password']):
            async with asyncpg.create_pool(POSTGRES_URI) as pool:
                async with pool.acquire() as conn:
                    row = await conn.fetchrow('SELECT id FROM user_auth WHERE user_id=$1', data['user_id'])
                    if not row:
                        await conn.execute('INSERT INTO user_auth (user_id, login, password) VALUES ($1, $2, $3)', data['user_id'], data['login'], data['password'])
                        await message.answer("✅Данные сохранены в боте.")
                    else:
                        await message.answer("❌Вы уже ввели свои данные")
        else:
            await message.answer("❌Неверный логин или пароль")
    await state.finish()






