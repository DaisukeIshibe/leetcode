import pandas as pd
'''
Customer table:
+-------------+--------------+--------------+-------------+
| customer_id | name         | visited_on   | amount      |
+-------------+--------------+--------------+-------------+
| 1           | Jhon         | 2019-01-01   | 100         |
| 2           | Daniel       | 2019-01-02   | 110         |
| 3           | Jade         | 2019-01-03   | 120         |
| 4           | Khaled       | 2019-01-04   | 130         |
| 5           | Winston      | 2019-01-05   | 110         | 
| 6           | Elvis        | 2019-01-06   | 140         | 
| 7           | Anna         | 2019-01-07   | 150         |
| 8           | Maria        | 2019-01-08   | 80          |
| 9           | Jaze         | 2019-01-09   | 110         | 
| 1           | Jhon         | 2019-01-10   | 130         | 
| 3           | Jade         | 2019-01-10   | 150         | 
+-------------+--------------+--------------+-------------+
'''
customer = pd.DataFrame({
	'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3],
	'name': ['Jhon', 'Daniel', 'Jade', 'Khaled', 'Winston', 'Elvis', 'Anna', 'Maria', 'Jaze', 'Jhon', 'Jade'],
	'visited_on': ['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08', '2019-01-09', '2019-01-10', '2019-01-10'],
	'amount': [100, 110, 120, 130, 110, 140, 150, 80, 110, 130, 150]
})

# You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).
# Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.
# Return the result table ordered by visited_on in ascending order.

customer['visited_on'] = pd.to_datetime(customer['visited_on'])
customer = customer.sort_values('visited_on')

customer['average_amount'] = customer['amount'].rolling(window=7, min_periods=1).mean().round(2)

result = customer[['visited_on', 'average_amount']].dropna().reset_index(drop=True)
print(result)