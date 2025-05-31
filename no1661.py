import pandas as pd
'''
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
+------------+------------+---------------+-----------+
| machine_id | process_id | activity_type | timestamp |
+------------+------------+---------------+-----------+
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
| 1          | 1          | start         | 0.430     |
| 1          | 1          | end           | 1.420     |
| 2          | 0          | start         | 4.100     |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.500     |
| 2          | 1          | end           | 5.000     |
+------------+------------+---------------+-----------+
'''
machine_df = pd.DataFrame({
	'machine_id': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
	'process_id': [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
	'activity_type': ['start', 'end', 'start', 'end', 'start', 'end', 'start', 'end', 'start', 'end', 'start', 'end'],
	'timestamp': [0.712, 1.520, 3.140, 4.120, 0.550, 1.550, 0.430, 1.420, 4.100, 4.512, 2.500, 5.000]
})

ids_df = machine_df.groupby(['machine_id', 'process_id']).agg(
	activity_type=('activity_type', lambda x: x.tolist()),
	timestamp=('timestamp', lambda x: x.tolist())
).reset_index()

# If activitity_type has 'start' and 'end', then the timestamp should be the first and last element of the list
ids_df['timestamp'] = ids_df['timestamp'].apply(lambda x: x[-1] - x[0] if len(x) == 2 else x)

print(ids_df)
# Calculate the average timestamp for each machine_id's process_id
out_df = ids_df.groupby('machine_id')['process_id'].apply(
	lambda x: pd.Series({
		'process_id': x.tolist(),
		'activity_type': ids_df.loc[x.index, 'activity_type'].tolist(),
		'timestamp': ids_df.loc[x.index, 'timestamp'].mean()
	})
).reset_index()
print(out_df)