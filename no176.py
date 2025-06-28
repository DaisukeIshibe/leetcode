import pandas as pd
'''
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
'''
employees_df = pd.DataFrame({
	'id': [1, 2, 3],
	'salary': [100, 200, 300]
})

salary_list = list(set(employees_df['salary'].tolist()))
out_df = pd.DataFrame(columns=['SecondHighestSalary'])
if len(salary_list) < 2:
	pass

second_highest = sorted(salary_list)[-2]
out_df = pd.DataFrame({'SecondHighestSalary': [second_highest]})
print(out_df)