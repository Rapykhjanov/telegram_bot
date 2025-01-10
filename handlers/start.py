from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "🍴 Добро пожаловать в наш ресторан!  \n "
        "Я — ваш виртуальный помощник и помогу:\n ")