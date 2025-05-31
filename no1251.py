import pandas as pd
'''
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
+------------+------------+------------+--------+
| product_id | start_date | end_date   | price |
| ---------- | ---------- | ---------- | ----- |
| 1          | 2019-02-17 | 2019-02-28 | 5     |
| 1          | 2019-03-01 | 2019-03-22 | 20    |
| 2          | 2019-02-01 | 2019-02-20 | 15    |
| 2          | 2019-02-21 | 2019-03-31 | 30    |
| 3          | 2019-02-21 | 2019-03-31 | 30    |
+------------+------------+------------+--------+

+------------+---------------+-------+
| product_id | purchase_date | units |
| ---------- | ------------- | ----- |
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |
+------------+---------------+-------+
'''
#product_df = pd.DataFrame({
#	'product_id': [1, 1, 2, 2],
#	'start_date': ['2019-02-17', '2019-03-01', '2019-02-01', '2019-02-21'],
#	'end_date': ['2019-02-28', '2019-03-22', '2019-02-20', '2019-03-31'],
#	'price': [5, 20, 15, 30]
#})
product_df = pd.DataFrame({
	'product_id': [1, 1, 2, 2, 3],
	'start_date': ['2019-02-17', '2019-03-01', '2019-02-01', '2019-02-21', '2019-02-21'],
	'end_date': ['2019-02-28', '2019-03-22', '2019-02-20', '2019-03-31', '2019-03-31'],
	'price': [5, 20, 15, 30, 30]
})
#unit_df = pd.DataFrame({
#	'product_id': [1, 1, 2, 2],
#	'purchase_date': ['2019-02-25', '2019-03-01', '2019-02-10', '2019-03-22'],
#	'units': [100, 15, 200, 30]
#})
unit_df = pd.DataFrame({
	'product_id': [1, 1, 2, 2],
	'purchase_date': ['2019-02-25', '2019-03-01', '2019-02-10', '2019-03-22'],
	'units': [100, 15, 200, 30]
})

product_df['start_date'] = pd.to_datetime(product_df['start_date'])
product_df['end_date'] = pd.to_datetime(product_df['end_date'])

if len(unit_df) == 0:
	out_df = product_df.groupby('product_id').apply(
		lambda x: pd.Series({
			'average_price': 0
		})
	).reset_index()
	print(out_df)

unit_df['purchase_date'] = pd.to_datetime(unit_df['purchase_date'])

# Merge the two DataFrames on product_id with OR condition and filter by date range
merged_df = pd.merge(unit_df, product_df, on='product_id', how='right')
# If there is nan in purchase_date, we can fill it with the start_date
merged_df['purchase_date'] = merged_df['purchase_date'].fillna(merged_df['start_date'])
merged_df['units'] = merged_df['units'].fillna(0)
merged_df = merged_df[
	(merged_df['purchase_date'] >= merged_df['start_date']) &
	(merged_df['purchase_date'] <= merged_df['end_date'])
]

merged_df['sell_price'] = merged_df['units'] * merged_df['price']
print(merged_df)
total_df = merged_df.groupby('product_id').agg(
		total_units=('units', 'sum'),
		total_sell_price=('sell_price', 'sum')
).reset_index()
print(total_df)
total_df['average_price'] = total_df.apply(
	lambda x: x['total_sell_price'] / x['total_units'] if x['total_units'] > 0 else 0, axis=1
)
total_df['average_price'] = total_df['average_price'].round(2)
# Format the average_price to 2 decimal places
print(total_df[['product_id','average_price']])