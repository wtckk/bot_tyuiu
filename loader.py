from aiogram import Bot, types, Dispatcher

from utils.db_api.db_gino import db
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)


__all__ = ['bot', 'dp', 'db']