import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
'''
employees_df = pd.DataFrame({
	'empId': [3, 1, 2, 4],
	'name': ['Brad', 'John', 'Dan', 'Thomas'],
	'supervisor': [None, 3, 3, 3],
	'salary': [4000, 1000, 2000, 4000]
})
bonus_df = pd.DataFrame({
	'empId': [2, 4],
	'bonus': [500, 2000]
})

merged_df = pd.merge(employees_df, bonus_df, on='empId', how='left')
out_df = merged_df[merged_df['bonus'].isnull() | (merged_df['bonus'] < 1000)][['name', 'bonus']]
print(out_df)