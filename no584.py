import pandas as pd
import numpy as np

'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+

+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
'''

customer_df = pd.DataFrame(
	{
		'id': [1, 2, 3, 4, 5, 6],
		'name': ['Will', 'Jane', 'Alex', 'Bill', 'Zack', 'Mark'],
		'referee_id': ['null', 'null', 2, 'null', 1, 2]
	}
)

print(customer_df)

# Name without being refereed by id:2.

out_df = customer_df[customer_df['referee_id'] != 2]
out_df = out_df[['name']]
print(out_df, type(out_df))