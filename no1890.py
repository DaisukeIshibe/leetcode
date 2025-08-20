import pandas as pd
'''
Logins table:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 6       | 2020-06-30 15:06:07 |
| 6       | 2021-04-21 14:06:06 |
| 6       | 2019-03-07 00:18:15 |
| 8       | 2020-02-01 05:10:53 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
| 2       | 2019-08-25 07:59:08 |
| 14      | 2019-07-14 09:00:00 |
| 14      | 2021-01-06 11:59:59 |
+---------+---------------------+
'''
# Write a solution to report the latest login for all users in the year 2020. Do not include the users who did not login in 2020.
logins = pd.DataFrame({
    'user_id': [6, 6, 6, 8, 8, 2, 2, 14, 14],
    'time_stamp': [
        '2020-06-30 15:06:07',
        '2021-04-21 14:06:06',
        '2019-03-07 00:18:15',
        '2020-02-01 05:10:53',
        '2020-12-30 00:46:50',
        '2020-01-16 02:49:50',
        '2019-08-25 07:59:08',
        '2019-07-14 09:00:00',
        '2021-01-06 11:59:59'
    ]
})
logins['time_stamp'] = pd.to_datetime(logins['time_stamp'])
latest_logins = logins[logins['time_stamp'].dt.year == 2020].sort_values('time_stamp').groupby('user_id').last().reset_index()
# Rename the columns
latest_logins.columns = ['user_id', 'last_login']
print(latest_logins)