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
| ---------- | ------ | ------ | ------ |
| 38         | 109    | 742    | 130    |
| 40         | null   | null   | 604    |
| 67         | null   | 681    | 332    |
| 99         | 66     | null   | 286    |
+------------+--------+--------+--------+
'''
products_df = pd.DataFrame({
	'product_id': [0, 1],
	'store1': [95, 70],
	'store2': [100, None],
	'store3': [105, 80]
})
#products_df = pd.DataFrame({
#	'product_id': [38, 40, 67, 99],
###	'store3': [130, 604, 332, 286]
#})

store_df = products_df.melt(id_vars=['product_id'], var_name='store', value_name='price')
store_df = store_df.dropna(subset=['price']).sort_values(by='product_id')
print(store_df)