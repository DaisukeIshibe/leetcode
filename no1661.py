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
| ---------- | ---------- | ------------- | --------- |
| 0          | 1          | start         | 18.891    |
| 1          | 0          | end           | 81.874    |
| 0          | 0          | start         | 37.019    |
| 0          | 1          | end           | 38.098    |
| 1          | 0          | start         | 25.135    |
| 1          | 1          | start         | 23.355    |
| 0          | 0          | end           | 40.222    |
| 1          | 1          | end           | 90.302    |
+------------+------------+---------------+-----------+
'''
#machine_df = pd.DataFrame({
#	'machine_id': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
#	'process_id': [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
#	'activity_type': ['start', 'end', 'start', 'end', 'start', 'end', 'start', 'end', 'start', 'end', 'start', 'end'],
#	'timestamp': [0.712, 1.520, 3.140, 4.120, 0.550, 1.550, 0.430, 1.420, 4.100, 4.512, 2.500, 5.000]
#})
machine_df = pd.DataFrame({
	'machine_id': [0, 1, 0, 0, 1, 1, 0, 1],
	'process_id': [1, 0, 0, 1, 0, 1, 0, 1],
	'activity_type': ['start', 'end', 'start', 'end', 'start', 'start', 'end', 'end'],
	'timestamp': [18.891, 81.874, 37.019, 38.098, 25.135, 23.355, 40.222, 90.302]
})

ids_df = machine_df.groupby(['machine_id', 'process_id']).agg(
	activity_type=('activity_type', lambda x: x.tolist()),
	timestamp=('timestamp', lambda x: x.tolist())
).reset_index()

# If activitiy_type is in the order 'end', 'start', then swap the order in the timestamp list
ids_df['timestamp'] = ids_df.apply(
	lambda row: row['timestamp'][::-1] if row['activity_type'] == ['end', 'start'] else row['timestamp'], axis=1
)

# If activitity_type has 'start' and 'end', then the timestamp should be the first and last element of the list
ids_df['each_processing_time'] = ids_df['timestamp'].apply(lambda x: x[-1] - x[0] if len(x) == 2 else x)
print(ids_df)

out_df = ids_df.groupby('machine_id').agg(
	processing_time=('each_processing_time', 'mean')
).round(3)
out_df = out_df.reset_index()
print(out_df)