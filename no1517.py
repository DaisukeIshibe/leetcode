import pandas as pd
'''
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 2       | Jonathan  | jonathanisgreat         |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
| 5       | Marwan    | quarz#2020@leetcode.com |
| 6       | David     | david69@gmail.com       |
| 7       | Shapiro   | .shapo@leetcode.com     |
+---------+-----------+-------------------------+
'''
user_df = pd.DataFrame({
	'user_id': [1, 2, 3, 4, 5, 6, 7],
	'name': ['Winston', 'Jonathan', 'Annabelle', 'Sally', 'Marwan', 'David', 'Shapiro'],
	'mail': [
		'winston@leetcode.com',
		'jonathanisgreat',
		'bella-@leetcode.com',
		'sally.come@leetcode.com',
		'quarz#2020@leetcode.com',
		'david69@gmail.com',
		'.shapo@leetcode.com']
})
valid_list:list = []
for _, rows in user_df.iterrows():
	mail = rows['mail']
	flag: bool = True
	if mail.startswith('.') or mail.startswith('#') or mail.startswith('@'):
		flag = False
	else:
		mail_body_list = mail.split('@')
		if len(mail_body_list) != 2:
			flag = False
		else:
			if mail_body_list[-1] == 'leetcode.com':
				name = mail_body_list[0]
				if '#' in name or '$' in name or '%' in name or '^' in name or '&' in name or '*' in name or ' ' in name:
					flag = False
				else:
					flag = True
			else:
				flag = False
	valid_list.append(flag)

# Extract valid emails
user_df = user_df[valid_list]
print(user_df)