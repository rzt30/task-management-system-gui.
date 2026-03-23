import sqlite3

def connect():
    return sqlite3.connect("tasks.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT,
        due_date TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_task(title, description, status, due_date):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks (title, description, status, due_date)
    VALUES (?, ?, ?, ?)
    """, (title, description, status, due_date))

    conn.commit()
    conn.close()

def get_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def update_task(task_id, title, description, status, due_date):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET title=?, description=?, status=?, due_date=?
    WHERE id=?
    """, (title, description, status, due_date, task_id))

    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    conn.commit()
    conn.close()