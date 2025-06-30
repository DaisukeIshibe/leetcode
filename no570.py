import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
'''
employees_df = pd.DataFrame({
	'id': [101, 102, 103, 104, 105, 106],
	'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'],
	'department': ['A', 'A', 'A', 'A', 'A', 'B'],
	'managerId': [None, 101, 101, 101, 101, 101]
})

m_dict = {}
for _, rows in employees_df.iterrows():
	manager_id = rows['managerId']
	if not manager_id in m_dict:
		m_dict[manager_id] = 1
	else:
		m_dict[manager_id] += 1

m_list = [k for k, v in m_dict.items() if v >= 5]
out_df = pd.DataFrame({
	'name': employees_df[employees_df['id'].isin(m_list)]['name'],
})
print(out_df)