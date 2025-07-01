import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
'''
person_df = pd.DataFrame({
	'id': [1, 2, 3],
	'email': ['a@b.com', 'c@d.com', 'a@b.com']
})

duplicated_emails = person_df[person_df.duplicated(['email'], keep=False)]
dup_mail_list = duplicated_emails['email'].unique()
out_df = pd.DataFrame({
	'Email': dup_mail_list,
})