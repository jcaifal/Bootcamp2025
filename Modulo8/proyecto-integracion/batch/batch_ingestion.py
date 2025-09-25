import pandas as pd
import json
import os

# Define file paths for CSV and JSON files
csv_file_path = 'data_source_1.csv'
json_file_path = 'data_source_2.json'

# Function to load and validate CSV data
def load_and_validate_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    
    df_csv = pd.read_csv(file_path)
    df_csv.columns = [col.strip().lower() for col in df_csv.columns]
    df_csv.dropna(subset=['id', 'name'], inplace=True)
    return df_csv

# Function to load and validate JSON data
def load_and_validate_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"JSON file not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data_json = json.load(f)
    
    df_json = pd.DataFrame(data_json)
    df_json.columns = [col.strip().lower() for col in df_json.columns]
    df_json.dropna(subset=['id', 'name'], inplace=True)
    return df_json

# Load and process both sources
try:
    df_csv = load_and_validate_csv(csv_file_path)
    df_json = load_and_validate_json(json_file_path)

    combined_df = pd.concat([df_csv, df_json], ignore_index=True)
    combined_df.to_csv('combined_data.csv', index=False)
    print("Data integration completed successfully. Output saved to 'combined_data.csv'.")

except Exception as e:
    print(f"Error during data integration: {e}")
