import sqlite3
from typing import Tuple, List
from sqlite3 import Connection, Cursor
from faker import Faker


def connect_to_db() -> Tuple[Connection, Cursor]:
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    return connection, cursor


def create_table() -> None:
    connection, cursor = connect_to_db()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
    )
    connection.commit()
    connection.close()


def insert_data() -> None:
    connection, cursor = connect_to_db()
    fake = Faker()
    for _ in range(100):
        cursor.execute(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            (fake.name(), fake.random_int(min=18, max=80))
        )
    connection.commit()
    connection.close()


def select_data() -> List[Tuple[str, int]]:
    connection, cursor = connect_to_db()
    cursor.execute("SELECT name, age FROM users WHERE age > 30")
    users = cursor.fetchall()
    connection.close()
    return users


if __name__ == "__main__":
    create_table()
    insert_data()
    print(select_data())
