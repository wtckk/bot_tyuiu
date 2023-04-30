from aiogram.types import CallbackQuery

from keyboards.inline import ikb_info
from loader import dp
from aiogram import types


@dp.message_handler(text='📖 Справочник')
async def info_inl(message: types.Message):
    await message.answer('Выберите интересующий вас раздел', reply_markup=ikb_info)
    await message.delete()

@dp.callback_query_handler(text='educon')
async def educon(call: CallbackQuery):
    await call.message.answer("EDUCON - системы поддержки учебного процесса, в которой хранятся лекции, тесты, лабораторные работы и всё, что может помочь, как студентам, так и преподавателям💻💾\n\
    \nМожно выполнять задания на самом сайте или же прикреплять туда лабораторные и домашние работы📑📘\n \
    \nЧтоб зайти в едукон, необходимо:\
    \n\t\t🔹Перейти по ссылке: https://educon2.tyuiu.ru\
    \n\t\t🔹Ввести логин и пароль, которые Вы получили на почту")


@dp.callback_query_handler(text='modeus')
async def modeus(call: CallbackQuery):
    await call.message.answer("Modeus - это основная платформа для работы студента ТИУ, там же Вы можете просмотреть расписание и сделать выбор курсов📚\n\
    \nЗайти можно, как со смартфона, так и с компьютера:\n\
    \n🔸Перейти по ссылке:\
    \n\t📱 http://m-tyuiu.modeus.org\
    \n\t💻 http://tyuiu.modeus.org\
    \n🔸Ввести std\логин и пароль, которые Вы получили на почту")


@dp.callback_query_handler(text='library')
async def library(call: CallbackQuery):
    await call.message.answer("Электронная библиотека ТИУ — это информационно-поисковая система, которая содержит:\n "
                              "\n🔴Информацию о традиционных ресурсах библиотеки (книги, журналы, диски и т.д.) – "
                              "библиографические записи, количество экземпляров, места хранения и пр.\n \n🔴Полные "
                              "тексты внутривузовских изданий ТИУ, выпускных квалификационных работ, журналов, "
                              "издаваемых Вузом.n\ \n🔴Библиографические записи со ссылкой перехода на полные тексты "
                              "из подписных электронных библиотечных систем (ЭБС). \nЧтобы получить доступ к "
                              "электронной библиотеки необходимо: \n\t🔺Перейти по ссылке http://webirbis.tsogu.ru "
                              "\n\t🔺Ввести логин и пароль, который Вы можете получить на информационно-библиотечное "
                              "занятии или в библиотеке по адресу Мельникайте 72")
