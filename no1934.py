import pandas as pd
'''
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
| action         | ENUM     |
+----------------+----------+
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |
+---------+---------------------+
+---------+---------------------+-----------+
| user_id | time_stamp          | action    |
+---------+---------------------+-----------+
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-02-28 23:59:59 | timeout   |
+---------+---------------------+-----------+
'''
signups_df = pd.DataFrame({
	'user_id': [3, 7, 2, 6],
	'time_stamp': ['2020-03-21 10:16:13', '2020-01-04 13:57:59', '2020-07-29 23:09:44', '2020-12-09 10:39:37']
})
confirmations_df = pd.DataFrame({
	'user_id': [3, 3, 7, 7, 7, 2, 2],
	'time_stamp': ['2021-01-06 03:30:46', '2021-07-14 14:00:00', '2021-06-12 11:57:29', '2021-06-13 12:58:28', '2021-06-14 13:59:27', '2021-01-22 00:00:00', '2021-02-28 23:59:59'],
	'action': ['timeout', 'timeout', 'confirmed', 'confirmed', 'confirmed', 'confirmed', 'timeout']
})

user_id_dict = {user_id: True for user_id in signups_df['user_id'].tolist()}
user_count_dict = {user_id : confirmations_df['user_id'].tolist().count(user_id) for user_id in user_id_dict.keys()}
rate_dict = {}
for user_id in user_id_dict.keys():
	rate_dict[user_id] = 0

user_action_dict = {}
for user_id in user_id_dict.keys():
	confirmed_count = confirmations_df[confirmations_df['user_id'] == user_id]['action'].tolist().count('confirmed')
	print(f'user_id: {user_id}, action_confirmed: {confirmed_count} user_count: {user_count_dict[user_id]}')
	rate = confirmed_count / user_count_dict[user_id] if user_count_dict[user_id] > 0 else 0
	# Round float value to 2 decimal places
	rate_dict[user_id] = f'{rate:.2f}'

out_df = pd.DataFrame({
	'user_id': list(user_id_dict.keys()),
	'confirmation_rate': [rate_dict[user_id] for user_id in user_id_dict.keys()]
})

print(out_df)