import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS survey_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    contact TEXT,
                    food_rating INTEGER,
                    extra_comments TEXT
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS dishes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    food_name TEXT NOT NULL,
                    food_description TEXT,
                    price FLOAT NOT NULL
                )
            """)
            conn.commit()

    def dishes(self, data: dict):
        try:
            with sqlite3.connect(self.path) as conn:
                conn.execute(
                    """
                    INSERT INTO dishes 
                    (food_name, food_description, price)
                    VALUES (?, ?, ?)
                    """,
                    (
                        data.get("food_name"),  # Название блюда
                        data.get("food_description"),  # Описание блюда
                        data.get("price")  # Цена блюда
                    )
                )
                conn.commit()
        except Exception as e:
            print(f"Ошибка при добавлении блюда: {e}")





























































# import sqlite3
#
#
# class Database:
#     def __init__(self, path: str):
#         self.path = path
#
#     def create_tables(self):
#         with sqlite3.connect(self.path) as conn:
#             conn.execute("""
#                 CREATE TABLE IF NOT EXISTS survey_results (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT,
#                     contact TEXT,
#                     food_rating INTEGER,
#                     extra_comments TEXT
#                 )
#             """)
#             conn.execute("""
#                 CREATE TABLE IF NOT EXISTS dish (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     food_name TEXT,
#                     price FLOAT,
#                     description TEXT,
#                     category TEXT,
#                     portion TEXT
#                 )
#             """)
#             conn.execute("""
#                 CREATE TABLE IF NOT EXISTS dishes (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     food_name TEXT NOT NULL,
#                     food_description TEXT,
#                     price FLOAT NOT NULL
#                 )
#             """)
#             conn.commit()
#
#     def save_survey(self, data: dict):
#         with sqlite3.connect(self.path) as conn:
#             conn.execute(
#                 """
#                 INSERT INTO survey_results
#                 (name, contact, food_rating, extra_comments)
#                 VALUES (?, ?, ?, ?)
#                 """,
#                 (
#                     data.get("name"),
#                     data.get("contact"),
#                     int(data.get("food_rating")),
#                     data.get("extra_comments")
#                 )
#             )
#             conn.commit()
#
#     def save_dish(self, data: dict):
#         with sqlite3.connect(self.path) as conn:
#             conn.execute(
#                 """
#                 INSERT INTO dish
#                 (food_name, price, description, category, portion)
#                 VALUES (?, ?, ?, ?, ?)
#                 """,
#                 (
#                     data.get("food_name"),
#                     data.get("price"),
#                     data.get("description"),
#                     data.get("category"),
#                     data.get("portion")
#                 )
#             )
#             conn.commit()
#
#     def dishes(self, data: dict):
#         with sqlite3.connect(self.path) as conn:
#             conn.execute(
#                 """
#                 INSERT INTO dishes
#                 (food_name, food_description, price)
#                 VALUES (?, ?, ?)
#                 """,
#                 (
#                     data.get("name"),  # Получаем название блюда
#                     data.get("description"),  # Получаем описание блюда
#                     data.get("price")  # Получаем цену
#                 )
#             )
#             conn.commit()
#
#     def save_dishes_list(self):
#         with sqlite3.connect(self.path) as conn:
#             conn.row_factory = sqlite3.Row
#             result = conn.execute("SELECT * FROM dishes")
#             data = result.fetchall()
#             return [dict(row) for row in data]
#
#     def get_menu_list(self):
#         with sqlite3.connect(self.path) as conn:
#             conn.row_factory = sqlite3.Row
#             result = conn.execute("SELECT * FROM dish")
#             data = result.fetchall()
#             return [dict(row) for row in data]
