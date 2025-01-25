from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from bot_config import database

dishes_router = Router()


class DishFSM(StatesGroup):
    name = State()
    description = State()
    price = State()


@dishes_router.message(Command(commands=["add_dish"]))
async def start_add_dish(message: types.Message, state: FSMContext):
    await message.answer("Введите название блюда:")
    await state.set_state(DishFSM.name)


@dishes_router.message(DishFSM.name)
async def enter_dish_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите описание блюда:")
    await state.set_state(DishFSM.description)


@dishes_router.message(DishFSM.description)
async def enter_dish_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите цену блюда (в формате 123.45):")
    await state.set_state(DishFSM.price)


@dishes_router.message(DishFSM.price)
async def enter_dish_price(message: types.Message, state: FSMContext):
    try:

        price = float(message.text)
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом.")

        await state.update_data(price=price)
        data = await state.get_data()

        database.save_to_dishes({
            "food_name": data.get("name"),
            "food_description": data.get("description"),
            "price": data.get("price"),
        })

        await message.answer(f"Блюдо '{data['name']}' успешно добавлено!")
        await state.clear()

    except ValueError:

        await message.answer("Ошибка! Введите корректную цену")

    except Exception as e:

        await message.answer(f"Произошла ошибка при добавлении блюда: {e}")
