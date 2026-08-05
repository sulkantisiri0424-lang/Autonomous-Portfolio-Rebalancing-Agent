import sqlite3

DATABASE = "portfolio.db"

def connect_database():
    connection = sqlite3.connect(DATABASE)
    return connection

def create_table():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS portfolio (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stock TEXT,
        allocation REAL
    )
    """)

    connection.commit()
    connection.close()
