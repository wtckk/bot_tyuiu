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
from time import sleep
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

    s = r"C:\parser\chromeDriver\chromedriver.exe"

    driver = webdriver.Chrome(
        executable_path=s,
        options=options
    )

    link = "https://tyuiu.modeus.org"
    try:

        driver.get(link)
        sleep(1)

        button = driver.find_element(By.XPATH, '//*[@id="bySelection"]/div[3]')
        button.click()
        sleep(1)

        login_input = driver.find_element(By.ID, "userNameInput")
        login_input.send_keys(fr"std\{login}")
        password_input = driver.find_element(By.ID, "passwordInput")
        password_input.send_keys(fr"{password}")
        sleep(5)

        submitButton = driver.find_element(By.ID, "submitButton")
        submitButton.click()
        sleep(10)

        select = Select(driver.find_element(By.CSS_SELECTOR, ".fc-view-select"))
        select.select_by_value("agendaDay")
        sleep(10)

        events = driver.find_elements(By.CSS_SELECTOR, "a.fc-time-grid-event")
        events_text = ""
        for event in events:
            text = event.text
            events_text += f"- {text}\n"

        # next_day_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "span.fc-icon-right-single-arrow")))
        # next_day_button.click()
        # sleep(5)

        await message.answer(events_text, parse_mode=ParseMode.HTML)
    except Exception as ex:
        await message.answer("Что-то пошло не так...")
    finally:
        driver.close()
        driver.quit()
