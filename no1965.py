import pandas as pd

'''
+-------------+----------+
| employee_id | name     |
+-------------+----------+
| 2           | Crew     |
| 4           | Haven    |
| 5           | Kristian |
+-------------+----------+
Write a solution to report the IDs of all the employees with missing information. The information of an employee is missing if:

The employee's name is missing, or
The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.
'''

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
	merged = employees.merge(salaries, on='employee_id', how='outer')
	missing_info = merged[(merged['name'].isnull()) | (merged['salary'].isnull())]
	result = missing_info[['employee_id']].drop_duplicates().sort_values(by='employee_id').reset_index(drop=True)
	return result