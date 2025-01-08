import asyncio
from aiogram import Dispatcher, types, Bot
from aiogram.filters import Command
import random

token = "8099448692:AAFMdfN_yypWuYlC6s8peqQpP2qzc2lbk_g"
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await bot.send_message(message.chat.id, f"Привет {name}\n"
                                            f"У меня есть команды : /myinfo, /random")


@dp.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    name = message.from_user.first_name
    id = message.from_user.id
    useer = message.from_user.username
    await message.answer(
        f"Имя: {name}! \n"
        f" id : {id} \n "
        f"Ваш ник : {useer} \n")


@dp.message(Command("random"))
async def random_handler(message: types.Message):
    random_name = ["Александр", "Мария", "Дмитрий", "Анна", "Сергей", "Екатерина", "Иван", "Ольга", "Максим", "Юлия"]
    selected_name = random.choice(random_name)
    await message.answer(f"Случайное имя: {selected_name}")

@dp.message()
async def echo_handler(message):
    await message.answer("Привет")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
