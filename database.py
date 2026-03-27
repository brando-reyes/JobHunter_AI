import sqlite3

def init_db():

    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_job(title):

    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO jobs (title, date) VALUES (?, datetime('now'))",
        (title,)
    )

    conn.commit()
    conn.close()