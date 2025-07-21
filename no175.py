import pandas as pd
'''
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+

Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+]
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
'''
person_df = pd.DataFrame({
	'personId': [1, 2],
	'lastName': ['Wang', 'Alice'],
	'firstName': ['Allen', 'Bob']
})
address_df = pd.DataFrame({
	'addressId': [1, 2],
	'personId': [2, 3],
	'city': ['New York City', 'Leetcode'],
	'state': ['New York', 'California']
})

merge_df = pd.merge(person_df, address_df, on='personId', how='left')
print(merge_df[['firstName', 'lastName', 'city', 'state']])