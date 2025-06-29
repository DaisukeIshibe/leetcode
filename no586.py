import pandas as pd
'''
+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+
'''
orders_df = pd.DataFrame({
	'order_number': [1, 2, 3, 4],
	'customer_number': [1, 2, 3, 3]
})

customer_list = list(set(orders_df['customer_number']))
if customer_list == []:
	print('No customers')
	out_df = pd.DataFrame({'customer_number': []})
	exit(0)
customer_oerder_dict = {c: orders_df['customer_number'].tolist().count(c) for c in customer_list}
# Extract the customer with the most orders
most_orders = max(customer_oerder_dict, key=customer_oerder_dict.get)
print(most_orders)
out_df = pd.DataFrame({'customer_number': [most_orders]})