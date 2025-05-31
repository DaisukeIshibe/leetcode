import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
+------------+------------+
| sell_date  | product     |
+------------+------------+
| 2020-05-30 | Headphone  |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible      |
| 2020-06-02 | Mask       |
| 2020-05-30 | T-Shirt    |
+------------+------------+
'''
sell_df = pd.DataFrame({
	'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30'],
	'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt']
})

out_df = sell_df.groupby('sell_date').apply(lambda x: x['product'].tolist()).reset_index(name='products')
out_df['products'] = out_df['products'].apply(lambda x: ','.join(sorted(set(x))))
out_df['num_sold'] = out_df['products'].apply(len)
out_df = out_df[['sell_date', 'num_sold', 'products']]
print(out_df)