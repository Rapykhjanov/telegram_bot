from aiogram import Router, F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from bot_config import database

dish_router = Router()
dish_router.message.filter(F.from_user.id == 5439294222 )


class Dish(StatesGroup):
    food_name = State()
    price = State()
    description = State()
    category = State()
    portion = State()


@dish_router.message(Command("dish_add"))
async def start_dish(message: types.Message, state: FSMContext):
    await message.answer("Введите название блюда:")
    await state.set_state(Dish.food_name)


@dish_router.message(Dish.food_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите цену (число):")
    await state.set_state(Dish.price)


@dish_router.message(Dish.price)
async def process_price(message: types.Message, state: FSMContext):
    try:
        price = float(message.text)
        await state.update_data(price=price)
        await message.answer("Введите описание для блюда:")
        await state.set_state(Dish.description)
    except ValueError:
        await message.answer("Цена должна быть числом. Попробуйте ещё раз:")


@dish_router.message(Dish.description)
async def process_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите категорию (супы, вторые, горячие напитки, холодные напитки и т.д.):")
    await state.set_state(Dish.category)


@dish_router.message(Dish.category)
async def process_category(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer("Введите варианты порций:")
    await state.set_state(Dish.portion)


@dish_router.message(Dish.portion)
async def process_portion(message: types.Message, state: FSMContext):
    await state.update_data(portion=message.text)
    data = await state.get_data()

    # Отображение данных пользователю
    await message.answer(
        f"Название: {data['name']}\n"
        f"Цена: {data['price']}\n"
        f"Описание: {data['description']}\n"
        f"Категория: {data['category']}\n"
        f"Порции: {data['portion']}"
    )

    # Сохранение данных в базу
    database.save_dish(data)

    await message.answer("Спасибо, блюдо было сохранено!")
    await state.clear()
