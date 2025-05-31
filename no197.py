import pandas as pd
'''
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
'''
weather_df = pd.DataFrame({
	'id': [1, 2, 3, 4],
	'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
	'temperature': [10, 25, 20, 30]
})
#weather_df = pd.DataFrame({
#	'id': [1, 2],
#	'recordDate': ['2000-12-14', '2000-12-16'],
#	'temperature': [3, 5]
#})

import datetime
# Sort the DataFrame by 'recordDate'
weather_df['recordDate'] = pd.to_datetime(weather_df['recordDate'])
weather_df = weather_df.sort_values(by='recordDate')

# Check recordDate is sequencial
weather_df['recordDate'] = weather_df['recordDate'].dt.date
weather_df['recordDate'] = weather_df['recordDate'].apply(lambda x: datetime.datetime.strptime(str(x), '%Y-%m-%d').date())
# Calculate the delta of recordDate formatted as int
weather_df['diff_date'] = weather_df['recordDate'].diff().fillna(pd.Timedelta(seconds=0))

weather_df['diff'] = weather_df['temperature'].diff().fillna(0).astype(int)
print(weather_df)
out_df = weather_df[
	(weather_df['diff'] > 0) & (weather_df['diff_date'] == pd.Timedelta(days=1))
	][['id']]
print(out_df)