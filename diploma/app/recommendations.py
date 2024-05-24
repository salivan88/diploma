import os
import pandas as pd
from django.conf import settings
from sklearn.metrics.pairwise import cosine_similarity
from .models import UserMovie
from django.contrib import messages
from requests import request

def get_combined_ratings(user_id):
    # Path to the ratings.csv file
    ratings_file_path = os.path.join(settings.BASE_DIR, 'data', 'ratings.csv')
    
    # Query user-specific ratings from UserMovie
    user_movies = UserMovie.objects.all().values('user_id', 'movie_id', 'rating')
    user_movies_df = pd.DataFrame(list(user_movies))

    # Load ratings data from your ratings table (stored in ratings.csv)
    ratings_df = pd.read_csv(ratings_file_path)

    # Combine both DataFrames
    combined_df = pd.concat([user_movies_df, ratings_df], ignore_index=True)

    # Handle duplicates by averaging the ratings
    combined_df = combined_df.groupby(['user_id', 'movie_id'], as_index=False).rating.mean()

    return combined_df

def build_user_movie_matrix(combined_df):
    user_movie_matrix = combined_df.pivot(index='user_id', columns='movie_id', values='rating')
    user_movie_matrix = user_movie_matrix.fillna(0)
    return user_movie_matrix

def calculate_user_similarity(user_movie_matrix):
    user_similarity = cosine_similarity(user_movie_matrix)
    return user_similarity

def get_recommendations(user_id, user_similarity, user_movie_matrix, n_recommendations=5):
    user_index = user_movie_matrix.index.get_loc(user_id)
    similar_users = list(enumerate(user_similarity[user_index]))
    similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)[1:]

    recommended_movies = {}
    for similar_user in similar_users:
        similar_user_index = similar_user[0]
        similarity_score = similar_user[1]

        user_ratings = user_movie_matrix.iloc[similar_user_index]
        for movie_id, rating in user_ratings.items():
            if user_movie_matrix.iloc[user_index, user_movie_matrix.columns.get_loc(movie_id)] == 0:
                if movie_id not in recommended_movies:
                    recommended_movies[movie_id] = similarity_score * rating
                else:
                    recommended_movies[movie_id] += similarity_score * rating

    recommended_movies = sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)
    recommended_movie_ids = [movie_id for movie_id, _ in recommended_movies][:n_recommendations]

    return recommended_movie_ids

def recommend_movies_for_user(user_id, n_recommendations=5):
    combined_df = get_combined_ratings(user_id)
    user_movie_matrix = build_user_movie_matrix(combined_df)
    user_similarity = calculate_user_similarity(user_movie_matrix)
    
    recommendations = get_recommendations(user_id, user_similarity, user_movie_matrix, n_recommendations)
    return recommendations
