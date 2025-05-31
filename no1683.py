import pandas as pd

'''
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+

+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+
'''

tweet_df = pd.DataFrame({
	'tweet_id': [1, 2],
	'content': ['Let us Code', 'More than fifteen chars are here!']
})

out_df = tweet_df[tweet_df['content'].str.len() <= 15][['tweet_id']]