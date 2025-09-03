import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
data = {
    "Movie": [
        "Inception",
        "The Matrix",
        "Interstellar",
        "The Dark Knight",
        "Avengers: Endgame",
        "Iron Man",
        "Coco",
        "Inside Out",
    ],
    "Genre": [
        "Sci-Fi Thriller",
        "Sci-Fi Action",
        "Sci-Fi Adventure",
        "Action Crime",
        "Action Superhero",
        "Action_Superhero",
        "Animation Family",
        "Animation Comedy",
    ],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# TF-IDF Vectorization on Genre
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["Genre"])

# Cosine similarity between all movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies
def recommend_movie(title, df=df, cosine_sim=cosine_sim):
    if title not in df["Movie"].values:
        return ["Movie not found in database."]
    
    # Get index of the given movie
    idx = df[df["Movie"] == title].index[0]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort by similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Recommend top 3 similar movies (excluding the input movie itself)
    sim_scores = sim_scores[1:4]
    movie_indices = [i[0] for i in sim_scores]
    
    return df["Movie"].iloc[movie_indices].tolist()


if __name__ == "__main__":
    title = input("Enter a movie title: ").strip()
    print(recommend_movie(title))