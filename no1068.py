import pandas as pd

'''
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+

+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+

+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
'''

sales_df = pd.DataFrame({
	'sale_id': [1, 2, 7],
	'product_id': [100, 100, 200],
	'year': [2008, 2009, 2011],
	'quantity': [10, 12, 15],
	'price': [5000, 5000, 9000]
})

product_df = pd.DataFrame({
	'product_id': [100, 200, 300],
	'product_name': ['Nokia', 'Apple', 'Samsung']
})

out_df = sales_df.merge(product_df, on='product_id', how='inner')[['product_name', 'year', 'price']]
print(out_df)