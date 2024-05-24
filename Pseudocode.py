// Define data structures

class User:
    id
    watched_movies // List of movie IDs the user has watched


class Movie:
    id
    title
    genre
    rating


// Sample data
users = List of User objects
movies = List of Movie objects

// Function to calculate similarity between two users
function calculate_similarity(user1, user2):
    common_movies = user1.watched_movies ∩ user2.watched_movies
    all_movies = user1.watched_movies ∪ user2.watched_movies
    similarity = size(common_movies) / size(all_movies)
    return similarity

// Function to get movie recommendations for a user
function get_recommendations(target_user):
    similarity_scores = {}
    for user in users:
        if user.id != target_user.id:
            similarity_scores[user.id] = calculate_similarity(target_user, user)

    // Sort users by similarity score in descending order
    sorted_users = sort_by_value(similarity_scores, descending=True)

    recommended_movies = {}

    // Aggregate movies from top similar users
    for similar_user_id in sorted_users:
        similar_user = find_user_by_id(similar_user_id)
        for movie_id in similar_user.watched_movies:
            if movie_id not in target_user.watched_movies:
                if movie_id in recommended_movies:
                    recommended_movies[movie_id] += similarity_scores[similar_user_id]
                else:
                    recommended_movies[movie_id] = similarity_scores[similar_user_id]

    // Sort recommended movies by aggregated similarity score in descending order
    sorted_recommended_movies = sort_by_value(recommended_movies, descending=True)

    // Convert movie IDs to movie titles for output
    recommended_movie_titles = [find_movie_by_id(
        movie_id).title for movie_id in sorted_recommended_movies]

    return recommended_movie_titles

// Helper functions
function find_user_by_id(user_id):
    for user in users:
        if user.id == user_id:
            return user
    return null

function find_movie_by_id(movie_id):
    for movie in movies:
        if movie.id == movie_id:
            return movie
    return null

// Example usage
target_user = find_user_by_id(target_user_id)
recommendations = get_recommendations(target_user)
print("Recommended movies for user", target_user.id, ":", recommendations)
