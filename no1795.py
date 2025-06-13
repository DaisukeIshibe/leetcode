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
#products_df = pd.DataFrame({
#	'product_id': [0, 1],
#	'store1': [95, 70],
#	'store2': [100, None],
#	'store3': [105, 80]
#})
products_df = pd.DataFrame({
	'product_id': [38, 40, 67, 99],
	'store1': [109, None, None, 66],
	'store2': [742, None, 681, None],
	'store3': [130, 604, 332, 286]
})

products_t_df = products_df.T
products_t_df = products_t_df.drop(products_t_df.index[0])
columns = products_t_df.columns
t_df = pd.concat([products_t_df[i] for i in columns], axis=1)
t_df = t_df.reset_index()
id_list = [[i]*len(products_t_df[i]) for i in columns.to_list()]
id_list = [item for sublist in id_list for item in sublist]

out_df = pd.DataFrame(columns=['product_id', 'store', 'price'])
out_df['product_id'] = id_list
store_list = [[s]*columns.size for s in t_df['index'].to_list()]
store_list = [item for sublist in store_list for item in sublist]
price_list = [t_df[i].to_list() for i in columns]
price_list = [item for sublist in price_list for item in sublist]
out_df['store'] = store_list
out_df['price'] = price_list
out_df = out_df.dropna()
print(out_df)

'''
out_df.columns = ['store', 'price']
out_df['product_id'] = id_list
out_df = out_df[['product_id', 'store', 'price']]
out_df = out_df.dropna()
print(out_df)
'''