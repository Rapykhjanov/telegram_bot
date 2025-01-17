import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            conn.execute("""
            CREATE TABLE IF NOT EXISTS complaints(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                contact TEXT,
                food_rating INTEGER,
                complaint TEXT
            )
            """)

    def save_complaint(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO complaints 
                (name, contact, food_rating, complaint)
                VALUES (?, ?, ?, ?)
                """,
                (
                    data.get("name"),
                    data.get("contact"),
                    int(data.get("food_rating")),
                    data.get("complaint")
                )
            )
            conn.commit()

# conn = sqlite3.connect("db.sqlite")
# cursor = conn.cursor()
# with sqlite3.connect("db.sqlite") as conn:
#     cursor = conn.cursor()
#     conn.execute("""
#     CREATE TABLE IF NOT EXISTS complaints(

#     )
#     """)