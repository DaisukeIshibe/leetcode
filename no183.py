import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
'''
customers = pd.DataFrame({
	'id': [1, 2, 3, 4],
	'name': ['Joe', 'Henry', 'Sam', 'Max']
})
orders = pd.DataFrame({
	'id': [1, 2],
	'customerId': [3, 1]
})

merged_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
result_df = merged_df[merged_df['customerId'].isnull()][['name']].reset_index()
result_df = result_df.rename(columns={'name': 'Customers'})
print(result_df)