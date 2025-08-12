import pandas as pd
'''
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
'''
sales = pd.DataFrame({
	'sale_id': [1, 2, 7],
	'product_id': [100, 100, 200],
	'year': [2008, 2009, 2011],
	'quantity': [10, 12, 15],
	'price': [5000, 5000, 9000]
})

# Write a solution to find all sales that occurred in the first year each product was sold.
first_year_sales = sales[sales['year'] == sales.groupby('product_id')['year'].transform('min')]
# Output order is: product_id, first_year, quantity, and price
first_year_sales = first_year_sales[['product_id', 'year', 'quantity', 'price']]
# Rename the columns
first_year_sales.columns = ['product_id', 'first_year', 'quantity', 'price']
print(first_year_sales)