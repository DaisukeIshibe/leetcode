import pandas as pd
'''
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | null      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
'''
transactions_df = pd.DataFrame({
	'id': [121, 122, 123, 124],
	'country': ['US', 'US', 'US', None],
	'state': ['approved', 'declined', 'approved', 'approved'],
	'amount': [1000, 2000, 2000, 2000],
	'trans_date': ['2018-12-18', '2018-12-19', '2019-01-01', '2019-01-07']
})

# Change the trans_date format from date to monthly
monthly_trans_df = transactions_df.copy()
monthly_trans_df['trans_date'] = pd.to_datetime(monthly_trans_df['trans_date']).dt.to_period('M').astype(str)

# If country is NaN, replace it with 'null'
monthly_trans_df['country'] = monthly_trans_df['country'].fillna('null')

# Group by month and country, then aggregate
out_df = monthly_trans_df.groupby(['trans_date', 'country']).agg(
	trans_count=('id', 'count'),
	approved_count=('state', lambda x: (x == 'approved').sum()),
	trans_total_amount=('amount', 'sum'),
	approved_total_amount=('amount', lambda x: x[monthly_trans_df.loc[x.index, 'state'] == 'approved'].sum())
).reset_index().rename(columns={'trans_date': 'month'})

# Reverse the "null" string to NaN
out_df['country'] = out_df['country'].replace('null', pd.NA)

# Display the final output DataFrame
print(out_df)