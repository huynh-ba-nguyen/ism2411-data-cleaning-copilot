# Purpose: Clean the raw sales data and save a processed version for analysis
import pandas as pd

# Import pandas and any other libraries needed
def clean_sales_data():
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
