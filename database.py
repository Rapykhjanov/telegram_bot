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

    def save_dish(self, data: dict):

        try:
            with sqlite3.connect(self.path) as conn:
                conn.execute(
                    """
                    INSERT INTO dishes
                    (food_name, food_description, price)
                    VALUES (?, ?, ?)
                    """,
                    (
                        data.get("food_name"),
                        data.get("food_description"),
                        data.get("price")
                    )
                )
                conn.commit()
        except Exception as e:
            print(f"Ошибка при добавлении блюда: {e}")

    def get_dishes(self):

        try:
            with sqlite3.connect(self.path) as conn:
                conn.row_factory = sqlite3.Row
                result = conn.execute("SELECT * FROM dishes")
                data = result.fetchall()
                return [dict(row) for row in data]
        except Exception as e:
            print(f"Ошибка при получении списка блюд: {e}")
            return []
