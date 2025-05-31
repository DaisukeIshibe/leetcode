import pandas as pd
'''
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
'''
user_df = pd.DataFrame({
	'user_id': [1, 2],
	'name': ['aLice', 'bOB']
})

def upper_head(name:str) -> str:
	return name[0].upper() + name[1:].lower()

user_df['name'] = user_df['name'].apply(upper_head)
user_df.sort_values(by='user_id', inplace=True)
print(user_df)