import pandas as pd
'''
+------------+---------+-----+
| student_id | name   | age  |
| ---------- | ------ | ---- |
| 355        | null   | 9    |
| 951        | null   | 8    |
| 470        | Quincy | 20   |
| 977        | Sophia | null |
| 300        | Liam   | 15   |
+------------+---------+-----+
'''
stdudents_df = pd.DataFrame({
	'student_id': [32, 217, 779, 849],
	'name': ['Piper', None, 'Georgia', 'Willow'],
	'age': [5, 19, 20, 14]
})

out_df = stdudents_df.dropna(subset=['name'])
print(out_df)