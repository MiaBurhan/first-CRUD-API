"""
This file is the ONLY place that touches the actual data.

Everything about how tasks are stored lives here.
"""

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]


def get_connection():
    return psycopg.connect(DATABASE_URL)


def initialize_database():
    """
    Create the database/table if they don't exist.
    Seed the three example tasks only if the table is empty.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT,
            done BOOLEAN
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany(
            "INSERT INTO tasks (title, done) VALUES (%s, %s)",
            [
                ("Learn SQLite", False),
                ("Build the tasks API", False),
                ("Test database persistence", False),
            ],
        )

    conn.commit()
    conn.close()


initialize_database()


def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "id": row[0],
            "title": row[1],
            "done": bool(row[2]),
        }
        for row in rows
    ]


def get_task_by_id(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = %s",
        (task_id,),
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "done": bool(row[2]),
    }


def create_task(title: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, done) VALUES (%s, %s) RETURNING id",
        (title, False),
    )

    task_id = cursor.fetchone()[0]

    conn.commit()
    conn.close()

    return {
        "id": task_id,
        "title": title,
        "done": False,
    }


def update_task(task_id: int, title: str, done: bool):
    """
    Update an existing task in the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET title = %s, done = %s WHERE id = %s",
        (title, done, task_id),
    )

    updated = cursor.rowcount > 0

    conn.commit()
    conn.close()

    if not updated:
        return None

    return get_task_by_id(task_id)


def delete_task(task_id: int):
    """
    Delete an existing task from the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,),
    )

    deleted = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return deleted