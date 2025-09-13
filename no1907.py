import pandas as pd
'''
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
'''
accounts = pd.DataFrame({
	'account_id': [3, 2, 8, 6],
	'income': [108939, 12747, 87709, 91796]
})
# Write a solution to calculate the number of bank accounts for each salary category.
# The salary categories are:
# "Low Salary": All the salaries strictly less than $20000.
# "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories. If there are no accounts in a category, return 0.
# Return the result table in any order.

# Extract the lowest, highest, and average salary categories with calculations
# Output table is as follows:
# +----------------+----------------+
# | category       | accounts_count |
# +----------------+----------------+
# | Low Salary     | 1              |
# | Average Salary | 0              |
# | High Salary    | 3              |
# +----------------+----------------+

low_salary_count = accounts[accounts['income'] < 20000].shape[0]
average_salary_count = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)].shape[0]
high_salary_count = accounts[accounts['income'] > 50000].shape[0]
result = pd.DataFrame({
	'category': ['Low Salary', 'Average Salary', 'High Salary'],
	'accounts_count': [low_salary_count, average_salary_count, high_salary_count]
})