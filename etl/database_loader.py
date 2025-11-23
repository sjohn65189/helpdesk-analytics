import sqlite3
import os

DB_PATH = "database/helpdesk.db"

def load_into_sql(df, table_name="incidents"):
    """
    Load a DataFrame into the existing SQLite database.
    """
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"{DB_PATH} not found. Run setup_database.py first.")

    conn = sqlite3.connect(DB_PATH)
    try:
        df.to_sql(table_name, conn, if_exists="append", index=False)
        print(f"[SQL] Loaded {len(df)} rows into table '{table_name}'")
    except Exception as e:
        print(f"[SQL] Error inserting into DB: {e}")
    finally:
        conn.close()
