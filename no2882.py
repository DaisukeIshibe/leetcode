import pandas as pd
'''
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
'''
custemer_df = pd.DataFrame({
	'customer_id': [1, 2, 3, 4, 5, 6],
	'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
	'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com'],
})

print(custemer_df.drop_duplicates(subset=['email']))