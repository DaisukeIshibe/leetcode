import pandas as pd
'''
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+
'''
salary_df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'C', 'D'],
    'sex': ['m', 'f', 'm', 'f'],
    'salary': [2500, 1500, 5500, 500]
})

print(salary_df)
for idx, row in salary_df.iterrows():
	if row['sex'] == 'm':
		salary_df.loc[idx, 'sex'] = 'f'
	elif row['sex'] == 'f':
		salary_df.loc[idx, 'sex'] = 'm'

print(salary_df)