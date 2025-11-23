import pandas as pd
import os

RAW_PATH = "data/raw/incidents_raw.csv"

def load_incidents(csv_path=RAW_PATH):
    """
    Load the raw incidents CSV into a pandas DataFrame.
    """
    if not os.path.exists(csv_path):
        print(f"[LOAD] File not found: {csv_path}")
        return pd.DataFrame()

    df = pd.read_csv(csv_path)
    print(f"[LOAD] Loaded {len(df)} rows from {csv_path}")
    return df
