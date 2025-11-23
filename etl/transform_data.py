import pandas as pd

def transform_incidents(df):
    """
    Apply business logic transformations:
    - SLA category based on ResolutionTime_Hours
    - Overdue flag (>48 hours)
    """
    df = df.copy()

    # SLA Category
    def sla_category(hours):
        if pd.isnull(hours):
            return "Unknown"
        elif hours <= 24:
            return "Fast"
        elif hours <= 48:
            return "Moderate"
        else:
            return "Slow"

    df["SLA_Category"] = df["ResolutionTime_Hours"].apply(sla_category)
    df["Overdue"] = df["ResolutionTime_Hours"] > 48

    print(f"[TRANSFORM] Added SLA_Category and Overdue columns")
    return df
