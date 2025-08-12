import pandas as pd
'''
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+
Product table:
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+
'''
customer = pd.DataFrame({
	'customer_id': [1, 2, 3, 3, 1],
	'product_key': [5, 6, 5, 6, 6]
})
product = pd.DataFrame({
	'product_key': [5, 6]
})

# report the customer ids from the Customer table that bought all the products in the Product table.
customer_product_df = customer[customer['product_key'].isin(product['product_key'])].groupby('customer_id').filter(lambda x: x['product_key'].nunique() == product['product_key'].nunique())
# extract the customer ids with DataFrame format
customer_ids = customer_product_df[['customer_id']].drop_duplicates()
print(customer_ids)