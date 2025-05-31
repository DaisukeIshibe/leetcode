import pandas as pd

'''
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+

Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+

EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
'''

employees_df = pd.DataFrame({
	'id': [1, 7, 11, 90, 3],
	'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
})

employees_unqi_df = pd.DataFrame({
	'id': [3, 11, 90],
	'unique_id': [1, 2, 3]
})

out_df = employees_df.merge(employees_unqi_df, on='id', how='left')
out_df = out_df[['unique_id', 'name']]
print(out_df)