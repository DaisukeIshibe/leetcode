import pandas as pd
'''
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
+-------------+-----------------------+------------------+
| product_id  | product_name          | product_category |
+-------------+-----------------------+------------------+
| 1           | Leetcode Solutions    | Book             |
| 2           | Jewels of Stringology | Book             |
| 3           | HP                    | Laptop           |
| 4           | Lenovo                | Laptop           |
| 5           | Leetcode Kit          | T-shirt          |
+-------------+-----------------------+------------------+
+--------------+--------------+----------+
| product_id   | order_date   | unit     |
+--------------+--------------+----------+
| 1            | 2020-02-05   | 60       |
| 1            | 2020-02-10   | 70       |
| 2            | 2020-01-18   | 30       |
| 2            | 2020-02-11   | 80       |
| 3            | 2020-02-17   | 2        |
| 3            | 2020-02-24   | 3        |
| 4            | 2020-03-01   | 20       |
| 4            | 2020-03-04   | 30       |
| 4            | 2020-03-04   | 60       |
| 5            | 2020-02-25   | 50       |
| 5            | 2020-02-27   | 50       |
| 5            | 2020-03-01   | 50       |
+--------------+--------------+----------+
'''
product_df = pd.DataFrame({
	'product_id': [1, 2, 3, 4, 5],
	'product_name': ['Leetcode Solutions', 'Jewels of Stringology', 'HP', 'Lenovo', 'Leetcode Kit'],
	'product_category': ['Book', 'Book', 'Laptop', 'Laptop', 'T-shirt']
})
order_df = pd.DataFrame({
	'product_id': [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5],
	'order_date': ['2020-02-05', '2020-02-10', '2020-01-18', '2020-02-11', '2020-02-17', '2020-02-24', 
	               '2020-03-01', '2020-03-04', '2020-03-04', '2020-02-25', '2020-02-27', '2020-03-01'],
	'unit': [60, 70, 30, 80, 2, 3, 20, 30, 60, 50, 50, 50]
})

order_df['order_date'] = pd.to_datetime(order_df['order_date'])
feb2020_df = order_df[(order_df['order_date'] >= pd.to_datetime('2020-02-01')) &
				 (order_df['order_date'] <= pd.to_datetime('2020-02-29'))]

extracted_order_df = pd.merge(product_df, feb2020_df, on='product_id', how='inner')
large_order_df = extracted_order_df.groupby('product_name').aggregate(total_unit=('unit', 'sum'))
large_order_df = large_order_df[large_order_df['total_unit'] >= 100].reset_index()
large_order_df = large_order_df.sort_values(by='total_unit')
large_order_df = large_order_df.rename(columns={'total_unit': 'unit'})
print(large_order_df)