import pandas as pd
'''
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
'''
students_df = pd.DataFrame({
	'student_id': [101, 53, 128, 3],
	'name': ['Ulysses', 'William', 'Henry', 'Henry'],
	'age': [13, 10, 6, 11]
})

out_df = students_df[students_df['student_id'] == 101][['name','age']].reset_index(drop=True)
print(out_df)