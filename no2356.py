import pandas as pd
'''
DaataFrame: teacher
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+

+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
'''
teacher_df = pd.DataFrame(
	{
		'teacher_id': [1, 1, 1, 2, 2, 2, 2],
		'subject_id': [2, 2, 3, 1, 2, 3, 4],
		'dept_id': [3, 4, 3, 1, 1, 1, 1]
	}
)
#print(teacher_df)

subject_df = teacher_df.groupby('teacher_id')['subject_id'].apply(set).reset_index()
subject_df['cnt'] = subject_df['subject_id'].apply(lambda x: len(x))
del subject_df['subject_id']
print(subject_df)