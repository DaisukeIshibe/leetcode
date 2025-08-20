import pandas as pd
'''
Users table:
+------------+--------------+
| account    | name         |
+------------+--------------+
| 900001     | Alice        |
| 900002     | Bob          |
| 900003     | Charlie      |
+------------+--------------+
Transactions table:
+------------+------------+------------+---------------+
| trans_id   | account    | amount     | transacted_on |
+------------+------------+------------+---------------+
| 1          | 900001     | 7000       |  2020-08-01   |
| 2          | 900001     | 7000       |  2020-09-01   |
| 3          | 900001     | -3000      |  2020-09-02   |
| 4          | 900002     | 1000       |  2020-09-12   |
| 5          | 900003     | 6000       |  2020-08-07   |
| 6          | 900003     | 6000       |  2020-09-07   |
| 7          | 900003     | -4000      |  2020-09-11   |
+------------+------------+------------+---------------+
'''
users = pd.DataFrame({
    'account': [900001, 900002, 900003],
    'name': ['Alice', 'Bob', 'Charlie']
})

transactions = pd.DataFrame({
    'trans_id': [1, 2, 3, 4, 5, 6, 7],
    'account': [900001, 900001, 900001, 900002, 900003, 900003, 900003],
    'amount': [7000, 7000, -3000, 1000, 6000, 6000, -4000],
    'transacted_on': [
        '2020-08-01',
        '2020-09-01',
        '2020-09-02',
        '2020-09-12',
        '2020-08-07',
        '2020-09-07',
        '2020-09-11'
    ]
})

# Write a solution to report the name and balance of users with a balance higher than 10000. The balance of an account is equal to the sum of the amounts of all transactions involving that account.
user_balances = transactions.groupby('account')['amount'].sum().reset_index()
user_balances = user_balances[user_balances['amount'] > 10000]
result = pd.merge(user_balances, users, on='account', how='inner')
print(result[['name', 'amount']].rename(columns={'amount': 'balance'}))