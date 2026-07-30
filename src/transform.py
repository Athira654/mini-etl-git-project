def transform_data(df):
    """
    Clean the customer data.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Standardize customer names
    df["name"] = df["name"].str.upper().str.strip()

    # Standardize city names
    df["city"] = df["city"].str.strip()

    print("\n===== DATA TRANSFORMED SUCCESSFULLY =====")
    print(f"Rows after cleaning: {len(df)}")

    return df