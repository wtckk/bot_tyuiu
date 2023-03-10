from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class isPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE
