import pandas as pd

'''
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+

+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
'''

viewer_df = pd.DataFrame({
	'article_id': [1, 1, 2, 2, 4, 3, 3],
	'author_id': [3, 3, 7, 7, 7, 4, 4],
	'viewer_id': [5, 6, 7, 6, 1, 4, 4],
	'view_date': ['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22', '2019-07-21', '2019-07-21']
})

out_df = viewer_df[viewer_df['author_id'] == viewer_df['viewer_id']][['author_id']].sort_values(by='author_id').drop_duplicates()
out_df = out_df.rename(columns={'author_id': 'id'})
print(out_df)