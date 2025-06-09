import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
'''
employee_df = pd.DataFrame({
	'employee_id': [2, 3, 7, 8, 9],
	'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
	'salary': [3000, 3800, 7400, 6100, 7700]
})

employee_list = employee_df['employee_id'].tolist()
out_df = pd.DataFrame(columns=['employee_id', 'bonus'])
out_df['employee_id'] = employee_list
out_df['bonus'] = 0
for idx, rows in employee_df.iterrows():
	employee_id, name, salary = rows
	if employee_id % 2 != 0:
		if name.startswith('M'):
			pass
		else:
			out_df.loc[idx, 'bonus'] = salary

out_df = out_df.sort_values(by='employee_id')
print(out_df)