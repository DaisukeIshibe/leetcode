import pandas as pd
'''
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
'''
products = pd.DataFrame({
	'product_id': [1, 2, 1, 1, 2, 3],
	'new_price': [20, 50, 30, 35, 65, 20],
	'change_date': ['2019-08-14', '2019-08-14', '2019-08-15', '2019-08-16', '2019-08-17', '2019-08-18']
})
# Initially, all products have price 10.
# Write a solution to find the prices of all products on the date 2019-08-16.
date = '2019-08-16'
mask = products['change_date'] <= date
filtered = products[mask]

# 2. 各product_idごとに最新の価格を取得
latest = filtered.sort_values('change_date').groupby('product_id', as_index=False).last()

# 3. すべてのproduct_idを取得し、初期値10でDataFrameを作成
all_ids = pd.Series(products['product_id'].unique())
result = pd.DataFrame({'product_id': all_ids, 'price': 10})

# 4. 最新価格で上書き
result = result.set_index('product_id')
latest = latest.set_index('product_id')
result.update(latest['new_price'].rename('price'))
result = result.reset_index()

print(result.sort_values('product_id'))	