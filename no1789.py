import pandas as pd
'''
+---------------+---------+
| Column Name   |  Type   |
+---------------+---------+
| employee_id   | int     |
| department_id | int     |
| primary_flag  | varchar |
+---------------+---------+
+-------------+---------------+--------------+
| employee_id | department_id | primary_flag |
+-------------+---------------+--------------+
| 1           | 1             | N            |
| 2           | 1             | Y            |
| 2           | 2             | N            |
| 3           | 3             | N            |
| 4           | 2             | N            |
| 4           | 3             | Y            |
| 4           | 4             | N            |
+-------------+---------------+--------------+
'''
employees_df = pd.DataFrame({
	'employee_id': [1, 2, 2, 3, 4, 4, 4],
	'department_id': [1, 1, 2, 3, 2, 3, 4],
	'primary_flag': ['N', 'Y', 'N', 'N', 'N', 'Y', 'N']
})

employee_list = list(set(employees_df['employee_id'].to_list()))

department_list = list(employees_df['department_id'].to_list())
primary_list = list(employees_df['primary_flag'].to_list())
dep_pri_dict:dict = {}
for d, p in zip(department_list, primary_list):
	if not dep_pri_dict:
		dep_pri_dict[d] = [p]
	else:
		dep_pri_dict[d].append(p)

