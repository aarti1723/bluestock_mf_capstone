import os
import pandas as pd

DATA_FOLDER = "data/raw"

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    print("=" * 80)
    print(f"FILE: {file}")

    file_path = os.path.join(DATA_FOLDER, file)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print("Error:", e)

    print("=" * 80)