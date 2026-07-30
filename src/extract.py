import pandas as pd

def extract_data():
    """
    Read customer data from CSV.
    """
    df = pd.read_csv("data/customers.csv")

    print("===== DATA EXTRACTED SUCCESSFULLY =====")
    print(f"Total Rows: {len(df)}")
    print(f"Total Columns: {len(df.columns)}")

    print("\nFirst 5 Records:\n")
    print(df.head())

    return df


if __name__ == "__main__":
    extract_data()