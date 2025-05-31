import pandas as pd

'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+

+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |
+----------+-------------+
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 5        | 200    |
| 12             | 1        | 910    |
| 13             | 2        | 970    |
+----------------+----------+--------+
'''
visits_df = pd.DataFrame({
	'visit_id': [1, 2, 4, 5, 6, 7, 8],
	'customer_id': [23, 9, 30, 54, 96, 54, 54]
})
transactions_df = pd.DataFrame({
	'transaction_id': [2, 3, 9, 12, 13],
	'visit_id': [5, 5, 5, 1, 2],
	'amount': [310, 300, 200, 910, 970]
})
c_df = pd.merge(visits_df, transactions_df, on='visit_id', how='left')[['customer_id', 'transaction_id']]
c_df = c_df[c_df['transaction_id'].isna()]
out_df = c_df.groupby('customer_id').size().reset_index(name='count_no_trans')
print(out_df)