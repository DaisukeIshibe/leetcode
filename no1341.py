import pandas as pd
'''
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+

+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+

+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  | 
| 2           | 2            | 2            | 2020-02-01  | 
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  | 
| 3           | 2            | 4            | 2020-02-25  | 
+-------------+--------------+--------------+-------------+
'''
movies = pd.DataFrame({
	'movie_id': [1, 2, 3],
	'title': ['Avengers', 'Frozen 2', 'Joker']
})
users = pd.DataFrame({
	'user_id': [1, 2, 3, 4],
	'name': ['Daniel', 'Monica', 'Maria', 'James']
})
movie_rating = pd.DataFrame({
	'movie_id': [1, 1, 1, 1, 2, 2, 2, 3, 3],
	'user_id': [1, 2, 3, 4, 1, 2, 3, 1, 2],
	'rating': [3, 4, 2, 1, 5, 2, 2, 3, 4],
	'created_at': ['2020-01-12', '2020-02-11', '2020-02-12', '2020-01-01',
		'2020-02-17', '2020-02-01', '2020-03-01', '2020-02-22', '2020-02-25']
})

# 1. User who rated the greatest number of movies
user_movie_counts = movie_rating.groupby('user_id')['movie_id'].nunique()
max_count = user_movie_counts.max()
top_users = user_movie_counts[user_movie_counts == max_count].index
top_user_names = users[users['user_id'].isin(top_users)]['name']
user_with_most_ratings = top_user_names.min()

# 2. Movie with highest average rating in Feb 2020
movie_rating['created_at'] = pd.to_datetime(movie_rating['created_at'])
feb_mask = (movie_rating['created_at'] >= '2020-02-01') & (movie_rating['created_at'] <= '2020-02-29')
feb_ratings = movie_rating[feb_mask]
avg_ratings = feb_ratings.groupby('movie_id')['rating'].mean()
if not avg_ratings.empty:
	max_avg = avg_ratings.max()
	top_movies = avg_ratings[avg_ratings == max_avg].index
	top_movie_titles = movies[movies['movie_id'].isin(top_movies)]['title']
	movie_with_highest_avg = top_movie_titles.min()
else:
	movie_with_highest_avg = None

# Result
result = pd.DataFrame({
	'results': [user_with_most_ratings, movie_with_highest_avg]
}, index=['user_with_most_ratings', 'movie_with_highest_average_rating_in_feb2020'])
print(result)