import pandas as pd
'''
DailySales table:
+-----------+-----------+---------+------------+
| date_id   | make_name | lead_id | partner_id |
+-----------+-----------+---------+------------+
| 2020-12-8 | toyota    | 0       | 1          |
| 2020-12-8 | toyota    | 1       | 0          |
| 2020-12-8 | toyota    | 1       | 2          |
| 2020-12-7 | toyota    | 0       | 2          |
| 2020-12-7 | toyota    | 0       | 1          |
| 2020-12-8 | honda     | 1       | 2          |
| 2020-12-8 | honda     | 2       | 1          |
| 2020-12-7 | honda     | 0       | 1          |
| 2020-12-7 | honda     | 1       | 2          |
| 2020-12-7 | honda     | 2       | 1          |
+-----------+-----------+---------+------------+
'''
daily_sales = pd.DataFrame({
	'date_id': ['2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7',
	            '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7'],
	'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota',
	              'honda', 'honda', 'honda', 'honda', 'honda'],
	'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
	'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]
})

# For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's
result = daily_sales.groupby(['date_id', 'make_name']).agg({
    'lead_id': 'nunique',
    'partner_id': 'nunique'
}).rename(columns={
    'lead_id': 'unique_leads',
    'partner_id': 'unique_partners'
}).reset_index()

print(result)

