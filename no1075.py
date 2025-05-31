import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+
'''
project_df = pd.DataFrame({
	'project_id': [1, 1, 1, 2, 2],
	'employee_id': [1, 2, 3, 1, 4]
})
employee_df = pd.DataFrame({
	'employee_id': [1, 2, 3, 4],
	'name': ['Khaled', 'Ali', 'John', 'Doe'],
	'experience_years': [3, 2, 1, 2]
})

employee_pj_df = pd.merge(project_df, employee_df, on='employee_id', how='inner')
d_df = employee_pj_df.groupby('project_id')['experience_years'].mean().reset_index()
d_df['average_years'] = d_df['experience_years'].round(2)
print(d_df[['project_id', 'average_years']])