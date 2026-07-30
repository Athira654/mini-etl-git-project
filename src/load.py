import os

def load_data(df):
    """
    Save the transformed data to the output folder.
    """

    # Create output folder if it doesn't exist
    os.makedirs("output", exist_ok=True)

    output_path = "output/cleaned_customers.csv"

    df.to_csv(output_path, index=False)

    print("\n===== DATA LOADED SUCCESSFULLY =====")
    print(f"File saved to: {output_path}")