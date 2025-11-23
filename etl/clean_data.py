import pandas as pd
import os

PROCESSED_PATH = "data/processed/incidents_cleaned.csv"

def clean_incidents(df, save_processed=True):
    """
    Clean incidents DataFrame:
    - Convert dates to datetime
    - Ensure numeric fields are numeric
    - Strip whitespace from string columns
    - Optionally save to processed folder
    """
    df = df.copy()

    # Convert dates
    df["DateCreated"] = pd.to_datetime(df["DateCreated"], errors="coerce")
    df["DateClosed"] = pd.to_datetime(df["DateClosed"], errors="coerce")

    # Ensure numeric
    df["ResolutionTime_Hours"] = pd.to_numeric(df["ResolutionTime_Hours"], errors="coerce")

    # Strip strings
    str_cols = ["IncidentID", "UserID", "AgentID", "Category", "Priority", "Status"]
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()

    # Drop rows without IncidentID
    df = df.dropna(subset=["IncidentID"])

    if save_processed:
        os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
        df.to_csv(PROCESSED_PATH, index=False)
        print(f"[CLEAN] Saved cleaned data to {PROCESSED_PATH}")

    print(f"[CLEAN] Cleaned DataFrame: {len(df)} rows remaining")
    return df
