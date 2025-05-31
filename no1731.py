import pandas as pd
'''
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
+-------------+---------+------------+-----+
| 1           | Michael | null       | 45  |
| 2           | Alice   | 1          | 38  |
| 3           | Bob     | 1          | 42  |
| 4           | Charlie | 2          | 34  |
| 5           | David   | 2          | 40  |
| 6           | Eve     | 3          | 37  |
| 7           | Frank   | null       | 50  |
| 8           | Grace   | null       | 48  |
+-------------+---------+------------+-----+
'''
#employee_df = pd.DataFrame({
#	'employee_id': [9, 6, 4, 2],
#	'name': ['Hercy', 'Alice', 'Bob', 'Winston'],
#	'reports_to': [None, 9, 9, None],
#	'age': [43, 41, 36, 37]
#})
employee_df = pd.DataFrame({
	'employee_id': [1, 2, 3, 4, 5, 6, 7, 8],
	'name': ['Michael', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
	'reports_to': [None, 1, 1, 2, 2, 3, None, None],
	'age': [45, 38, 42, 34, 40, 37, 50, 48]
})

reports_to_df = employee_df.dropna(subset=['reports_to'])
merged_df = pd.merge(reports_to_df, employee_df[['employee_id', 'name']], left_on='reports_to', right_on='employee_id', suffixes=('', '_boss'))
print(merged_df)
summary_df = merged_df.groupby(['employee_id_boss','name_boss']).agg(
	employee_count=('employee_id', 'count'),
	average_age=('age', 'mean')
).reset_index()
summary_df['average_age'] = summary_df['average_age'].apply(lambda x: round(x+0.5) if x % 1 >= 0.5 else round(x)).astype(int)
summary_df.rename(columns={'employee_id_boss': 'employee_id', 'name_boss': 'name', 'employee_count': 'reports_count'}, inplace=True)

print(summary_df)