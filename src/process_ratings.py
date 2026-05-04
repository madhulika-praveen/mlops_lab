import pandas as pd

def process_ratings(input_path, output_path):
    df = pd.read_csv(input_path)

    print(f"Original rows: {len(df)}")

    # Remove duplicates
    df = df.drop_duplicates()

    # Basic validation
    df = df[df["rating"].between(1.0, 5.0)]

    print(f"Cleaned rows: {len(df)}")

    df.to_csv(output_path, index=False)
    print(f"Saved cleaned data to {output_path}")


if __name__ == "__main__":
    process_ratings(
        "data/raw/ratings.csv",
        "data/processed/ratings_clean.csv"
    )