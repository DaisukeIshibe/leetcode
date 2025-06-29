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

employee_list = employees_df['employee_id'].to_list()
department_list = employees_df['department_id'].to_list()
primary_list = employees_df['primary_flag'].to_list()

uniq_employee_list = list(set(employee_list))
emp_dep_df = pd.DataFrame({
	'employee_id': uniq_employee_list,
	'department_id': [0] * len(uniq_employee_list)
})
for emp_id, dep_id, primary in zip(employee_list, department_list, primary_list):
	print(f"Employee ID: {emp_id}, Department ID: {dep_id}, Primary Flag: {primary}")
	emp_dep_df.loc[emp_dep_df['employee_id'] == emp_id, 'department_id'] = dep_id

for emp_id, dep_id, primary in zip(employee_list, department_list, primary_list):
	if primary == 'Y':
		emp_dep_df.loc[emp_dep_df['employee_id'] == emp_id, 'department_id'] = dep_id

print(emp_dep_df)