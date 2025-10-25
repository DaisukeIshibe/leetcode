import pandas as pd
'''
+------------------+------+
| Column Name      | Type | 
+------------------+------+
| transaction_id   | int  |
| amount           | int  |
| transaction_date | date |
+------------------+------+
The transactions_id column uniquely identifies each row in this table.
Each row of this table contains the transaction id, amount and transaction date.
Write a solution to find the sum of amounts for odd and even transactions for each day. If there are no odd or even transactions for a specific date, display as 0.

Return the result table ordered by transaction_date in ascending order.
Input:

transactions table:

+----------------+--------+------------------+
| transaction_id | amount | transaction_date |
+----------------+--------+------------------+
| 1              | 150    | 2024-07-01       |
| 2              | 200    | 2024-07-01       |
| 3              | 75     | 2024-07-01       |
| 4              | 300    | 2024-07-02       |
| 5              | 50     | 2024-07-02       |
| 6              | 120    | 2024-07-03       |
+----------------+--------+------------------+
  
Output:

+------------------+---------+----------+
| transaction_date | odd_sum | even_sum |
+------------------+---------+----------+
| 2024-07-01       | 75      | 350      |
| 2024-07-02       | 0       | 350      |
| 2024-07-03       | 0       | 120      |
+------------------+---------+----------+
'''
transactions = pd.DataFrame({
	'transaction_id': [1, 2, 3, 4, 5, 6],
	'amount': [100, 200, 150, 300, 250, 400],
	'transaction_date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03']
})

def sum_odd_even_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
	transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date'])
	transactions['odd_even'] = transactions['transaction_id'] % 2
	grouped = transactions.groupby(['transaction_date', 'odd_even'])['amount'].sum().unstack(fill_value=0).reset_index()
	grouped.columns = ['transaction_date', 'even_sum', 'odd_sum']
	return grouped[['transaction_date', 'odd_sum', 'even_sum']].sort_values('transaction_date')