import pandas as pd
import os

def load_data(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist!")
    return pd.read_csv(file_path)

def clean_column_names(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def clean_text_columns(df):
    if "product_name" in df.columns:
        df["product_name"] = df["product_name"].astype(str).str.strip()
    if "category" in df.columns:
        df["category"] = df["category"].astype(str).str.strip()
    return df

def handle_missing_values(df):
    df = df.dropna(subset=["price", "quantity"])
    return df

def remove_invalid_rows(df):
    df = df[(df["price"] >= 0) & (df["quantity"] >= 0)]
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df = load_data(raw_path)
    df = clean_column_names(df)
    df = clean_text_columns(df)
    df = handle_missing_values(df)
    df = remove_invalid_rows(df)

    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
     # Save cleaned data
    df.to_csv(cleaned_path, index=False)
    
    print("Cleaning complete. First few rows of cleaned data:")
    print(df.head())
