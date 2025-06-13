import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
'''
products_df = pd.DataFrame({
	'product_id': [0, 1],
	'store1': [95, 70],
	'store2': [100, None],
	'store3': [105, 80]
})

products_t_df = products_df.T
products_t_df = products_t_df.drop(products_t_df.index[0])
out_df = pd.concat([products_t_df[0], products_t_df[1]], axis=0)
out_df = out_df.reset_index()
out_df.columns = ['store', 'price']
out_df['product_id'] = 0
print(out_df)