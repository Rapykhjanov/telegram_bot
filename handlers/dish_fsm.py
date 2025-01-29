from aiogram import Router, F, types
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.fsm.context import FSMContext
from bot_config import database
from dotenv import dotenv_values

menu_management_router = Router()

menu_id = dotenv_values(".env")["ADMIN_ID"]


class Menu(StatesGroup):
    food_name = State()
    price = State()
    description = State()
    category = State()
    portion = State()
    cover = State()


@menu_management_router.callback_query(F.data == "menu", default_state)
async def create_menu(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == int(menu_id):
        await callback.message.answer("Введите название блюда: ")
        await state.set_state(Menu.food_name)
    else:
        await callback.answer("У вас нет прав для добавления меню.")


@menu_management_router.message(Menu.food_name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text.strip()
    await state.update_data(food_name=name)
    await message.answer("Введите цену (число): ")
    await state.set_state(Menu.price)


@menu_management_router.message(Menu.price)
async def process_price(message: types.Message, state: FSMContext):
    try:
        price = float(message.text.strip())
        await state.update_data(price=price)
        await message.answer("Введите описание для блюда: ")
        await state.set_state(Menu.description)
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число для цены.")


@menu_management_router.message(Menu.description)
async def process_description(message: types.Message, state: FSMContext):
    description = message.text.strip()
    await state.update_data(description=description)
    await message.answer("Введите категорию (супы, вторые, горячие напитки, холодные напитки и т.д.): ")
    await state.set_state(Menu.category)


@menu_management_router.message(Menu.category)
async def process_category(message: types.Message, state: FSMContext):
    category = message.text.strip()
    await state.update_data(category=category)
    await message.answer("Введите размер порции (например, 200г, 0.5л и т.д.): ")
    await state.set_state(Menu.portion)


@menu_management_router.message(Menu.portion)
async def process_portion(message: types.Message, state: FSMContext):
    portion = message.text.strip()
    await state.update_data(portion=portion)
    await message.answer("Теперь загрузите изображение блюда:")
    await state.set_state(Menu.cover)


@menu_management_router.message(Menu.cover)
async def process_cover(message: types.Message, state: FSMContext):
    if message.photo:
        # Берем фотографию в лучшем качестве
        photo = message.photo[-1]
        file_id = photo.file_id
        await state.update_data(cover=file_id)
        await finalize_menu_creation(message, state, cover=file_id)
    else:
        await message.answer("Пожалуйста, загрузите изображение блюда.")


async def finalize_menu_creation(message: types.Message, state: FSMContext, cover=None):
    data = await state.get_data()

    summary = (
        f"Спасибо за добавление блюда!\n"
        f"Название: {data.get('food_name')}\n"
        f"Цена: {data.get('price')}\n"
        f"Описание: {data.get('description')}\n"
        f"Категория: {data.get('category')}\n"
        f"Размер порции: {data.get('portion')}\n"
        f"Изображение добавлено!"
    )
    await message.answer(summary)

    try:
        data['cover'] = cover  # Добавляем ссылку на изображение в данные
        database.save_menu(data)
        await message.answer("Ваше блюдо сохранено!")
    except Exception as e:
        await message.answer(f"Ошибка сохранения блюда: {e}")

    await state.clear()






































