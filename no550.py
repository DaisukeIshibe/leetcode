import pandas as pd
'''
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
'''
activity = pd.DataFrame({
	'player_id': [1, 1, 2, 3, 3],
	'device_id': [2, 2, 3, 1, 4],
	'event_date': ['2016-03-01', '2016-03-02', '2017-06-25', '2016-03-02', '2018-07-03'],
	'games_played': [5, 6, 1, 0, 5]
})

# Convert event_date to datetime
activity['event_date'] = pd.to_datetime(activity['event_date'])

# Find the first login date for each player
first_login = activity.groupby('player_id')['event_date'].min().reset_index()
first_login.columns = ['player_id', 'first_login_date']

# Calculate the day after first login
first_login['day_after_first_login'] = first_login['first_login_date'] + pd.Timedelta(days=1)

# Merge with original activity data to check if players logged in the day after
merged = first_login.merge(activity, on='player_id', how='left')

# Check if players logged in on the day after their first login
consecutive_logins = merged[merged['event_date'] == merged['day_after_first_login']]

# Calculate the fraction
total_players = first_login['player_id'].nunique()
consecutive_players = consecutive_logins['player_id'].nunique()
fraction = round(consecutive_players / total_players, 2)

result = pd.DataFrame({'fraction': [fraction]})
print(result)
