import pandas as pd
'''
+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+
+--------+------------+---------+----------+
| emp_id | event_day  | in_time | out_time |
+--------+------------+---------+----------+
| 1      | 2020-11-28 | 4       | 32       |
| 1      | 2020-11-28 | 55      | 200      |
| 1      | 2020-12-03 | 1       | 42       |
| 2      | 2020-11-28 | 3       | 33       |
| 2      | 2020-12-09 | 47      | 74       |
+--------+------------+---------+----------+
'''
employee_df = pd.DataFrame({
	'emp_id': [1, 1, 1, 2, 2],
	'event_day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'],
	'in_time': [4, 55, 1, 3, 47],
	'out_time': [32, 200, 42, 33, 74]
})

employee_df['total_time'] = employee_df['out_time'] - employee_df['in_time']
out_df = employee_df.groupby(['emp_id', 'event_day']).agg({'total_time': 'sum'}).reset_index()
out_df = out_df.sort_values(by=['event_day','emp_id'])
out_df = out_df[['event_day', 'emp_id', 'total_time']]
out_df.columns = ['day', 'emp_id', 'total_time']
print(out_df)