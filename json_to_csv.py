import json
import pandas as pd

def json_array_to_csv(json_file, csv_file):
    """Converts the 'cars' array in a JSON file to a CSV, excluding the 'image' field."""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Extract the 'cars' array
        cars_array = data.get("cars", [])

        # Normalize the 'cars' array
        df = pd.json_normalize(cars_array)

        # Select columns to include (exclude 'image')
        columns_to_include = [col for col in df.columns if col != 'image']
        df_filtered = df[columns_to_include]

        df_filtered.to_csv(csv_file, index=False, encoding='utf-8')
        print(f"Successfully converted 'cars' array from {json_file} to {csv_file} (excluding 'image').")

    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
json_array_to_csv("data.json", "data.csv")