# Purpose: Clean the raw sales data and save a processed version for analysis
import pandas as pd
import os

# Import pandas and any other libraries needed
def load_data(file_path: str):
    return pd.read_csv(file_path)

def clean_column_names(df):
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

def clean_text_columns(df):
    df['product_name'] = df['product_name'].str.strip()
    df['category'] = df['category'].str.strip()
    return df

def handle_missing_values(df):
    df = df.dropna(subset=['price', 'quantity'])
    return df

def remove_invalid_rows(df):
    df = df[(df['price'] >= 0) & (df['quantity'] >= 0)]
    return df

def clean_sales_data():
    # Load the raw CSV file from the data/raw folder
    raw_data_path = 'data/raw/sales_data_raw.csv'
    df = load_data(raw_data_path)

    # Standardize column names to lowercase and use underscores
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    # Strip leading and trailing whitespace from product names and categories
    df['product_name'] = df['product_name'].str.strip()
    df['category'] = df['category'].str.strip()

    # Handle missing prices and quantities consistently (either drop or fill)
    df = df.dropna(subset=['price', 'quantity'])

    # Remove rows with negative prices or quantities
    df = df[(df['price'] >= 0) & (df['quantity'] >= 0)]

    # Save the cleaned data to the data/processed folder as sales_data_clean.csv
    processed_data_path = 'data/processed/sales_data_clean.csv'
    df.to_csv(processed_data_path, index=False)

# Load the raw CSV file from the data/raw folder
raw_data_path = 'data/raw/sales_data_raw.csv'
df = pd.read_csv(raw_data_path)

# Standardize column names to lowercase and use underscores
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# Strip leading and trailing whitespace from product names and categories
df['product_name'] = df['product_name'].str.strip()
df['category'] = df['category'].str.strip()

# Handle missing prices and quantities consistently (either drop or fill)
df = df.dropna(subset=['price', 'quantity'])

# Remove rows with negative prices or quantities
df = df[(df['price'] >= 0) & (df['quantity'] >= 0)]

# Save the cleaned data to the data/processed folder as sales_data_clean.csv
processed_data_path = 'data/processed/sales_data_clean.csv'
df.to_csv(processed_data_path, index=False)

df = load_data("data/raw/sales_data_raw.csv")
df = clean_column_names(df)
df = clean_text_columns(df)
df = handle_missing_values(df)
df = remove_invalid_rows(df)

os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/sales_data_clean.csv", index=False)

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

df_raw = load_data(raw_path)
df_clean = clean_column_names(df_raw)
df_clean = clean_text_columns(df_clean)
df_clean = handle_missing_values(df_clean)
df_clean = remove_invalid_rows(df_clean)

import os
os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
df_clean.to_csv(cleaned_path, index=False)

print("Cleaning complete. First few rows of cleaned data:")
print(df_clean.head())