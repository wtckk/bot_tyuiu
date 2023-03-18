from aiogram import Dispatcher


from .private_chat import isPrivate


def setup(dp: Dispatcher):
    dp.filters_factory.bind(isPrivate)