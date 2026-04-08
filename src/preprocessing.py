def preprocess_data(df):
    try:
        # Keep only numeric columns
        df = df.select_dtypes(include=['int64', 'float64'])

        # Fill missing values
        df = df.ffill().fillna(0)

        print("Preprocessing complete")
        return df

    except Exception as e:
        print(f"Preprocessing error: {e}")