from load_data import load_incidents
from clean_data import clean_incidents
from transform_data import transform_incidents
from database_loader import load_into_sql
from setup_database import create_database

def run_etl():
    print("[ETL] Starting ETL process...")

    # Step 0: Ensure database & tables exist
    create_database()

    # Step 1: Load raw CSV
    df = load_incidents()
    if df.empty:
        print("[ETL] No data to process. Exiting.")
        return

    # Step 2: Clean
    df = clean_incidents(df)

    # Step 3: Transform
    df = transform_incidents(df)

    # Step 4: Load into SQL
    load_into_sql(df)

    print("[ETL] ETL process completed successfully.")

if __name__ == "__main__":
    run_etl()
