import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def create_features(input_path, output_path):
    df = pd.read_csv(input_path)

    user_item_matrix = df.pivot_table(
        index='user_id',
        columns='movie_id',
        values='rating'
    ).fillna(0)

    similarity = cosine_similarity(user_item_matrix)

    with open(output_path, "wb") as f:
        pickle.dump(similarity, f)

    print(f"Saved similarity matrix to {output_path}")


if __name__ == "__main__":
    create_features(
        "data/processed/ratings_clean.csv",
        "models/user_similarity.pkl"
    )