import pandas as pd

'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+

+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
'''

product_df = pd.DataFrame(
	{
		'product_id': [0, 1, 2, 3, 4],
		'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
		'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
	}
)

#print(product_df)
low_rec_df = product_df[(product_df['low_fats'] == 'Y') & (product_df['recyclable'] == 'Y')]
print(low_rec_df['product_id'])