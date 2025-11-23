import sqlite3
import os

DB_PATH = "database/helpdesk.db"
SCHEMA_PATH = "database/schema.sql"

def create_database():
    """
    Create the SQLite database and tables from schema.sql.
    If database or tables already exist, do nothing.
    """
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())
    conn.close()
    print(f"[SETUP] Database created (or already exists) at {DB_PATH}")

if __name__ == "__main__":
    create_database()
