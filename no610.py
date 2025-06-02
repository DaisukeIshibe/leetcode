import pandas as pd
'''
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
'''
triangle_df = pd.DataFrame({
	'x': [13, 10],
	'y': [15, 20],
	'z': [30, 15]
})

triangle_df['triangle'] = 'No'
for idx, row in triangle_df.iterrows():
	x, y, z = row['x'], row['y'], row['z']
	if (x + y > z) and (x + z > y) and (y + z > x):
		triangle_df.loc[idx, 'triangle'] = 'Yes'
print(triangle_df)