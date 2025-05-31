import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
'''
mail_df = pd.DataFrame({
	'id': [1, 2, 3],
	'email': ['john@example.com','bob@example.com','john@example.com']
})
# Eliminate duplicate emails
mail_df = mail_df.drop_duplicates(subset='email')
print(mail_df)