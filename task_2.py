import sqlite3
from typing import Tuple, List
from sqlite3 import Connection, Cursor
from faker import Faker


def create_table() -> None:
    with sqlite3.connect("users.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
        )
        connection.commit()


def insert_data() -> None:
    fake = Faker()
    with sqlite3.connect("users.db") as connection:
        cursor = connection.cursor()
        for _ in range(100):
            cursor.execute(
                "INSERT INTO users (name, age) VALUES (?, ?)",
                (fake.name(), fake.random_int(min=18, max=80))
            )
        connection.commit()


def select_data() -> List[Tuple[str, int]]:
    with sqlite3.connect("users.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT name, age FROM users WHERE age > 30")
        users = cursor.fetchall()
    return users


if __name__ == "__main__":
    create_table()
    insert_data()
    print(select_data())
