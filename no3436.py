import pandas as pd
'''
Write a solution to find all the valid email addresses. A valid email address meets the following criteria:

It contains exactly one @ symbol.
It ends with .com.
The part before the @ symbol contains only alphanumeric characters and underscores.
The part after the @ symbol and before .com contains a domain name that contains only letters.
Return the result table ordered by user_id in ascending order.

 

Example:

Input:

Users table:

+---------+---------------------+
| user_id | email               |
+---------+---------------------+
| 1       | alice@example.com   |
| 2       | bob_at_example.com  |
| 3       | charlie@example.net |
| 4       | david@domain.com    |
| 5       | eve@invalid         |
+---------+---------------------+
Output:

+---------+-------------------+
| user_id | email             |
+---------+-------------------+
| 1       | alice@example.com |
| 4       | david@domain.com  |
+---------+-------------------+
Explanation:

alice@example.com is valid because it contains one @, alice is alphanumeric, and example.com starts with a letter and ends with .com.
bob_at_example.com is invalid because it contains an underscore instead of an @.
charlie@example.net is invalid because the domain does not end with .com.
david@domain.com is valid because it meets all criteria.
eve@invalid is invalid because the domain does not end with .com.
Result table is ordered by user_id in ascending order.

Example:

Input:

Users table:

+---------+---------------------+
| user_id | email               |
+---------+---------------------+
| 1       | alice@example.com   |
| 2       | bob_at_example.com  |
| 3       | charlie@example.net |
| 4       | david@domain.com    |
| 5       | eve@invalid         |
+---------+---------------------+
Output:

+---------+-------------------+
| user_id | email             |
+---------+-------------------+
| 1       | alice@example.com |
| 4       | david@domain.com  |
+---------+-------------------+
'''
users = pd.DataFrame({
	'user_id': [1, 2, 3, 4, 5],
	'email': ['alice@example.com', 'bob_at_example.com', 'charlie@example.net', 'david@domain.com', 'eve@invalid']
})

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
	import re

	def is_valid_email(email):
		pattern = r'^[A-Za-z0-9_]+@[A-Za-z]+\.(com)$'
		return re.match(pattern, email) is not None

	valid_emails = users[users['email'].apply(is_valid_email)]
	return valid_emails.sort_values(by='user_id').reset_index(drop=True)