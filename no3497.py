import pandas as pd
'''
+---------+---------------+---------------+-------------------+
| user_id | activity_date | activity_type | activity_duration |
+---------+---------------+---------------+-------------------+
| 1       | 2023-01-01    | free_trial    | 45                |
| 1       | 2023-01-02    | free_trial    | 30                |
| 1       | 2023-01-05    | free_trial    | 60                |
| 1       | 2023-01-10    | paid          | 75                |
| 1       | 2023-01-12    | paid          | 90                |
| 1       | 2023-01-15    | paid          | 65                |
| 2       | 2023-02-01    | free_trial    | 55                |
| 2       | 2023-02-03    | free_trial    | 25                |
| 2       | 2023-02-07    | free_trial    | 50                |
| 2       | 2023-02-10    | cancelled     | 0                 |
| 3       | 2023-03-05    | free_trial    | 70                |
| 3       | 2023-03-06    | free_trial    | 60                |
| 3       | 2023-03-08    | free_trial    | 80                |
| 3       | 2023-03-12    | paid          | 50                |
| 3       | 2023-03-15    | paid          | 55                |
| 3       | 2023-03-20    | paid          | 85                |
| 4       | 2023-04-01    | free_trial    | 40                |
| 4       | 2023-04-03    | free_trial    | 35                |
| 4       | 2023-04-05    | paid          | 45                |
| 4       | 2023-04-07    | cancelled     | 0                 |
+---------+---------------+---------------+-------------------+
A subscription service wants to analyze user behavior patterns. The company offers a 7-day free trial, after which users can subscribe to a paid plan or cancel. Write a solution to:

Find users who converted from free trial to paid subscription
Calculate each user's average daily activity duration during their free trial period (rounded to 2 decimal places)
Calculate each user's average daily activity duration during their paid subscription period (rounded to 2 decimal places)
Return the result table ordered by user_id in ascending order.
'''
user_activity = pd.DataFrame({
    'user_id': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4],
    'activity_date': ['2023-01-01', '2023-01-02', '2023-01-05', '2023-01-10', '2023-01-12', '2023-01-15',
                      '2023-02-01', '2023-02-03', '2023-02-07', '2023-02-10',
                      '2023-03-05', '2023-03-06', '2023-03-08', '2023-03-12', '2023-03-15', '2023-03-20',
                      '2023-04-01', '2023-04-03', '2023-04-05', '2023-04-07'],
    'activity_type': ['free_trial', 'free_trial', 'free_trial', 'paid', 'paid', 'paid',
                      'free_trial', 'free_trial', 'free_trial', 'cancelled',
                      'free_trial', 'free_trial', 'free_trial', 'paid', 'paid', 'paid',
                      'free_trial', 'free_trial', 'paid', 'cancelled'],
    'activity_duration': [45, 30, 60, 75, 90, 65, 55, 25, 50, 0,
                         70, 60, 80, 50, 55, 85, 40, 35, 45, 0]
})

# Convert activity_date to datetime
user_activity['activity_date'] = pd.to_datetime(user_activity['activity_date'])
# Identify users who converted from free trial to paid
converted_users = user_activity[user_activity['activity_type'] == 'paid']['user_id'].unique()
# Filter data for converted users
converted_data = user_activity[user_activity['user_id'].isin(converted_users)]

# Calculate average daily activity duration during free trial
free_trial_data = converted_data[converted_data['activity_type'] == 'free_trial']
paid_data = converted_data[converted_data['activity_type'] == 'paid']
avg_free_trial = free_trial_data.groupby('user_id')['activity_duration'].mean(2).reset_index()
avg_paid = paid_data.groupby('user_id')['activity_duration'].mean().round(2).reset_index()
# Merge results
result = avg_free_trial.merge(avg_paid, on='user_id', suffixes=('_free_trial', '_paid'))
# Rename columns
result.columns = ['user_id', 'avg_free_trial_duration', 'avg_paid_duration']
# Sort by user_id
result = result.sort_values(by='user_id').reset_index(drop=True)
# Result columns name is as follows:
# | user_id | trial_avg_duration | paid_avg_duration |
result.columns = ['user_id', 'trial_avg_duration', 'paid_avg_duration']
print(result)