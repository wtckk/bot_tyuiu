import random
import asyncpg

from data.config import POSTGRES_URI
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from aiogram.types import ParseMode
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery
from asyncio import sleep
from keyboards.inline import ikb_schedule
from data.config import POSTGRES_URI

import tracemalloc
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)


@dp.message_handler(text="📅 Расписание")
async def parse_schedule(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    try:
        async with asyncpg.create_pool(POSTGRES_URI) as pool:
            async with pool.acquire() as conn:
                result = await conn.fetchrow('select login, password FROM user_auth WHERE user_id=$1', user_id)
        login = result['login']
        password = result['password']
    except TypeError:
        await message.answer("Ваши данные не найдены...")

    options = webdriver.ChromeOptions()

    useragent = UserAgent()

    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")

    s = r"G:\Рабочий стол\bot_tyuiu\utils\parser_modeus"

    driver = webdriver.Chrome(
        executable_path=s,
        options=options
    )

    link = "https://tyuiu.modeus.org"
    try:

        driver.get(link)
        await sleep(1)

        button = driver.find_element(By.XPATH, '//*[@id="bySelection"]/div[3]')
        button.click()
        await sleep(1)

        login_input = driver.find_element(By.ID, "userNameInput")
        login_input.send_keys(fr"std\{login}")
        password_input = driver.find_element(By.ID, "passwordInput")
        password_input.send_keys(fr"{password}")
        await sleep(2)

        submitButton = driver.find_element(By.ID, "submitButton")
        submitButton.click()
        await sleep(5)

        select = Select(driver.find_element(By.CSS_SELECTOR, ".fc-view-select"))
        select.select_by_value("agendaDay")
        await sleep(2)

        events = driver.find_elements(By.CSS_SELECTOR, "a.fc-time-grid-event")
        events_text = ""
        for event in events:
            text = event.text
            events_text += f"- {text}\n"
        await message.answer(events_text, parse_mode=ParseMode.HTML, reply_markup=ikb_schedule)

    except Exception as ex:
        await message.answer("Что-то пошло не так...")
        print(ex)
    finally:
        driver.close()
        driver.quit()


@dp.callback_query_handler(lambda c: c.data in ['next_day', 'prev_day'])
async def process_choose_day(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    try:
        async with asyncpg.create_pool(POSTGRES_URI) as pool:
            async with pool.acquire() as conn:
                result = await conn.fetchrow('select login, password FROM user_auth WHERE user_id=$1', chat_id)
        login = result['login']
        password = result['password']
    except TypeError:
        await bot.answer_callback_query(callback_query.id, "Ваши данные не найдены...")
        return

    options = webdriver.ChromeOptions()

    useragent = UserAgent()

    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")

    s = r"G:\Рабочий стол\bot_tyuiu\utils\parser_modeus"

    driver = webdriver.Chrome(
        executable_path=s,
        options=options
    )

    link = "https://tyuiu.modeus.org"
    try:

        driver.get(link)
        await sleep(1)

        button = driver.find_element(By.XPATH, '//*[@id="bySelection"]/div[3]')
        button.click()
        await sleep(1)

        login_input = driver.find_element(By.ID, "userNameInput")
        login_input.send_keys(fr"std\{login}")
        password_input = driver.find_element(By.ID, "passwordInput")
        password_input.send_keys(fr"{password}")
        await sleep(3)

        submitButton = driver.find_element(By.ID, "submitButton")
        submitButton.click()
        await sleep(10)

        select = Select(driver.find_element(By.CSS_SELECTOR, ".fc-view-select"))
        select.select_by_value("agendaDay")
        await sleep(3)

        if callback_query.data == "next_day":
            print('next_day')
            next_day = driver.find_element(By.CSS_SELECTOR,
                                           '.fc-next-button.fc-button.fc-state-default.fc-corner-right')
            next_day.click()
            await sleep(5)

            events = driver.find_elements(By.CSS_SELECTOR, "a.fc-time-grid-event")
            events_text = "Расписание на следующий день\n"
            for event in events:
                text = event.text
                events_text += f"- {text}\n"

            await bot.send_message(chat_id=chat_id, text=events_text, parse_mode=ParseMode.HTML)
        elif callback_query.data == "prev_day":
            print("prev_Day")
            prev_day = driver.find_element(By.CSS_SELECTOR, '.fc-prev-button')
            prev_day.click()
            await sleep(5)

            events = driver.find_elements(By.CSS_SELECTOR, "a.fc-time-grid-event")
            events_text = "Расписание на предыдущий день\n"
            for event in events:
                text = event.text
                events_text += f"- {text}\n"
            await bot.send_message(chat_id=chat_id, text=events_text, parse_mode=ParseMode.HTML)

    except Exception as ex:
        await bot.answer_callback_query(callback_query.id, "Что-то пошло не так...")
        print(ex)
    finally:
        driver.close()
        driver.quit()
