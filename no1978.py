import pandas as pd
'''
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| manager_id  | int      |
| salary      | int      |
+-------------+----------+

+-------------+-----------+------------+--------+
| employee_id | name      | manager_id | salary |
+-------------+-----------+------------+--------+
| 3           | Mila      | 9          | 60301  |
| 12          | Antonella | null       | 31000  |
| 13          | Emery     | null       | 67084  |
| 1           | Kalel     | 11         | 21241  |
| 9           | Mikaela   | null       | 50937  |
| 11          | Joziah    | 6          | 28485  |
+-------------+-----------+------------+--------+
'''

employee_df = pd.DataFrame({
	'employee_id': [3, 12, 13, 1, 9, 11],
	'name': ['Mila', 'Antonella', 'Emery', 'Kalel', 'Mikaela', 'Joziah'],
	'manager_id': [9, None, None, 11, None, 6],
	'salary': [60301, 31000, 67084, 21241, 50937, 28485]
})

d_df = employee_df[employee_df['salary'] < 30000]
d_df = d_df.dropna(subset=['manager_id'])
# Check manager_id is not in employee_id
d_df = d_df[d_df['manager_id'].isin(employee_df['employee_id']) == False]
# Select only employee_id and name columns
print(d_df)