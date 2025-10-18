import pandas as pd
'''
Write a solution to find the employees who earn more than their managers.
Return the result table in any order.

Example 1:

Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
'''
employee = pd.DataFrame({
	'id': [1, 2, 3, 4],
	'name': ['Joe', 'Henry', 'Sam', 'Max'],
	'salary': [70000, 80000, 60000, 90000],
	'managerId': [3, 4, None, None]
})
# Merge the employee table with itself to get manager salaries
merged = employee.merge(employee[['id', 'salary']], left_on='managerId', right_on='id', suffixes=('', '_manager'))
# Find employees who earn more than their managers
result = merged[merged['salary'] > merged['salary_manager']][['name']]
result.rename(columns={'name': 'Employee'}, inplace=True)
print(result)