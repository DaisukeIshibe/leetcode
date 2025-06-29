import pandas as pd
'''
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+

+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+
'''
activity_df = pd.DataFrame({
	'user_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
	'session_id': [1, 1, 1, 4, 4, 4, 2, 2, 2, 3, 3],
	'activity_date': ['2019-07-20', '2019-07-20', '2019-07-20',
					  '2019-07-20', '2019-07-21', '2019-07-21',
					  '2019-07-21', '2019-07-21', '2019-07-21',
					  '2019-06-25', '2019-06-25'],
	'activity_type': ['open_session', 'scroll_down', 'end_session',
					  'open_session', 'send_message', 'end_session',
					  'open_session', 'send_message', 'end_session',
					  'open_session', 'end_session']
})


activity_df['activity_date'] = pd.to_datetime(activity_df['activity_date'])
uniq_user_list = activity_df['user_id'].unique()
user_activity_dict = {}
for user_id in uniq_user_list:
	user_sessions = activity_df[activity_df['user_id'] == user_id]
	user_activity_dict[user_id] = []
	for _, row in user_sessions.iterrows():
		date = row['activity_date'].date()
		# Check if the date is before 2019-07-27 - 30 days
		if date < (pd.to_datetime('2019-07-27') - pd.Timedelta(days=30)).date():
			continue
		# Skip if the date is after 2019-07-27
		if date > pd.to_datetime('2019-07-27').date():
			continue
		user_activity_dict[user_id].append(date)

for k, v in user_activity_dict.items():
	user_activity_dict[k] = [d for d in list(set(v))]

# Convert the datetime.date objects to strings
active_date_list = [d for v in user_activity_dict.values() for d in v]
uniq_date_list = list(set(active_date_list))
out_df = pd.DataFrame({
	# Convert datetime.date objects to strings for the output
	'day': uniq_date_list,
	'active_users': [''] * len(uniq_date_list)
})
for u in uniq_date_list:
	count = active_date_list.count(u)
	out_df.loc[out_df['day'] == u, 'active_users'] = count
out_df['day'] = out_df['day'].astype(str)  # Convert to string for output

print(out_df)