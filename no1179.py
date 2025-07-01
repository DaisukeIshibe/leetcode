import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| revenue     | int     |
| month       | varchar |
+-------------+---------+
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+
'''
department_df = pd.DataFrame({
	'id': [1, 2, 3, 1, 1],
	'revenue': [8000, 9000, 10000, 7000, 6000],
	'month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar']
})

id_list = department_df['id'].unique().tolist()
for id in id_list:
	month_df = department_df[department_df['id'] == id]
	print(month_df[['month', 'revenue']].T)