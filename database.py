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
                CREATE TABLE IF NOT EXISTS dish (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    food_name TEXT,
                    price FLOAT,
                    description TEXT,
                    category TEXT,
                    portion TEXT)
                        """)
            conn.commit()

    def save_survey(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO survey_results 
                (name, contact, food_rating,  extra_comments)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    data.get("name"),
                    data.get("contact"),
                    int(data.get("food_rating")),
                    data.get("extra_comments")

            )
            )
            conn.commit()

    def save_dish(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO dish 
                (food_name, price, description, category,portion)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    data.get("food_name"),
                    data.get("price"),
                    data.get("description"),
                    data.get("category"),
                    data.get("portion")
                )
            )
            conn.commit()

    def get_menu_list(self):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute("SELECT * from menu")
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            # data = result.fetchmany(10)

            return [dict(row) for row in data]
