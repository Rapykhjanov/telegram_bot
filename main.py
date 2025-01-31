import asyncio
import logging
from aiogram import Bot
from bot_config import bot, dp, database
from handlers.start import start_router
from handlers.random import random_router
from handlers.myinfo import myinfo_router
from handlers.other_massages import echo_router
from handlers.review_dialog import review_router
from handlers.dish_fsm import menu_management_router
from handlers.dishes import menu_list_router
from handlers.group_managament import group_router



async def on_startup(bot: Bot):
    try:

        database.create_tables()
        logging.info("Таблицы успешно созданы.")
    except Exception as e:
        logging.error(f"Ошибка при создании таблиц: {e}")


async def main():
    try:

        dp.include_router(review_router)
        dp.include_router(random_router)
        dp.include_router(myinfo_router)
        dp.include_router(start_router)
        dp.include_router(menu_management_router)
        dp.include_router(menu_list_router)
        dp.include_router(echo_router)
        dp.include_router(group_router)
 
        dp.startup.register(on_startup)

        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    asyncio.run(main())
