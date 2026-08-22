import os
import pandas as pd

def extract(file_path: str) -> pd.DataFrame:
    """Extract raw dataset from local or remote path."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found: {file_path}")
    print(f"[EXTRACT] Loading data from {file_path}...")
    return pd.read_csv(file_path)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Clean missing values and standardize column data types."""
    print("[TRANSFORM] Cleaning missing values and structuring schema...")
    df = df.dropna().drop_duplicates()
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def load(df: pd.DataFrame, output_path: str) -> None:
    """Export processed dataset to structured storage."""
    print(f"[LOAD] Writing structured output to {output_path}...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print("[LOAD] Pipeline execution complete.")

if __name__ == "__main__":
    input_file = "house_data.csv"
    output_file = "processed_house_data.csv"
    
    raw_data = extract(input_file)
    cleaned_data = transform(raw_data)
    load(cleaned_data, output_file)
