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
salary_df = pd.DataFrame({
	'id': [1, 2, 3],
	'salary': [100, 200, 300]
})

def nth_highest_salary(salary_df, N):
	# Get the unique salaries in descending order
	unique_salaries = salary_df['salary'].drop_duplicates().sort_values(ascending=False)
	
	out_df = pd.DataFrame(columns=[f'getNthHighestSalary({N})'])
	# Check if N is within the range of unique salaries
	if N <= len(unique_salaries):
		# Get the N-th highest salary
		nth_salary = unique_salaries.iloc[N - 1]
		out_df[f'getNthHighestSalary({N})'] = [nth_salary]
		return out_df
	else:
		return out_df

print(nth_highest_salary(salary_df, 2))  # Output: 200	