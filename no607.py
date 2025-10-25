import pandas as pd
'''
Table: Company

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+
com_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a company and the city in which the company is located.
 

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+
order_id is the primary key (column with unique values) for this table.
com_id is a foreign key (reference column) to com_id from the Company table.
sales_id is a foreign key (reference column) to sales_id from the SalesPerson table.
Each row of this table contains information about one order. This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.
 

Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".
'''
sales_person = pd.DataFrame({
	'sales_id': [1, 2, 3, 4],
	'name': ['Alice', 'Bob', 'Charlie', 'David']
})
company = pd.DataFrame({
	'com_id': [1, 2, 3],
	'name': ['RED', 'BLUE', 'GREEN'],
	'city': ['New York', 'Los Angeles', 'Chicago']
})
orders = pd.DataFrame({
	'order_id': [101, 102, 103, 104],
	'order_date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
	'com_id': [1, 2, 2, 3],
	'sales_id': [1, 2, 3, 4],
	'amount': [500, 300, 400, 600]
})

# Find the com_id for the company named "RED"
red_com_id = company[company['name'] == 'RED']['com_id'].iloc[0]
# Find sales_ids who have orders related to the company "RED"
sales_with_red_orders = orders[orders['com_id'] == red_com_id]['sales_id'].unique()
# Find all sales_ids
all_sales_ids = sales_person['sales_id'].unique()
# Find sales_ids who do not have orders related to the company "RED"
sales_without_red_orders = all_sales_ids[~np.isin(all_sales_ids, sales_with_red_orders)]
# Find names of salespersons who do not have orders related to the company "RED"
sales_person[sales_person['sales_id'].isin(sales_without_red_orders)]
# Output the result
result = sales_person[sales_person['sales_id'].isin(sales_without_red_orders)][['name']]
print(result)