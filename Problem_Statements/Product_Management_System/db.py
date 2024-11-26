import sqlite3

# Initialize the SQLite database
def initialize_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            productId INTEGER PRIMARY KEY,
            productName TEXT NOT NULL,
            productPrice REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

initialize_db()
