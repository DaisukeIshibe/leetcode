import pandas as pd
'''
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |
+----+------------+-------------+--------+
'''
movie_df = pd.DataFrame({
	'id': [1, 2, 3, 4, 5],
	'movie': ['War', 'Science', 'irish', 'Ice song', 'House card'],
	'description': ['great 3D', 'fiction', 'boring', 'Fantacy', 'Interesting'],
	'rating': [8.9, 8.5, 6.2, 8.6, 9.1]
})

out_df = movie_df[
	(movie_df['id'] % 2 == 1) & (movie_df['description'].str.contains('boring') == False)
	].sort_values(by='id', ascending=False).reset_index(drop=True)
print(out_df)