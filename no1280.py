import pandas as pd
'''
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
+------------+--------------+
| student_id | subject_name |
+------------+--------------+
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |
+------------+--------------+
'''
students_df = pd.DataFrame({
	'student_id': [1, 2, 13, 6],
	'student_name': ['Alice', 'Bob', 'John', 'Alex']
})
subjects_df = pd.DataFrame({
	'subject_name': ['Math', 'Physics', 'Programming']
})
examinations_df = pd.DataFrame({
	'student_id': [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
	'subject_name': ['Math', 'Physics', 'Programming', 'Programming', 'Physics', 'Math', 'Math', 'Programming', 'Physics', 'Math', 'Math']
})

from collections import OrderedDict

student_dict = OrderedDict()
for _, rows in examinations_df.iterrows():
	student_id = rows['student_id']
	subject_name = rows['subject_name']
	if not student_id in student_dict:
		student_dict[student_id] = [subject_name]
	else:
		student_dict[student_id].append(subject_name)

stduent_id_list = students_df['student_id'].tolist()
for s_id in stduent_id_list:
	if not s_id in student_dict:
		student_dict[s_id] = []

# Sort the dictionary by student_id
student_dict = OrderedDict(sorted(student_dict.items()))

# Create an output DataFrame
data_len = len(student_dict) * len(subjects_df)
output_df = pd.DataFrame({
	'student_id': [k for k in student_dict.keys() for _ in subjects_df['subject_name']],
	'student_name': [''] * data_len,
	'subject_name': [''] * data_len,
	'attended_exams': [0] * data_len
})

subjects_df = subjects_df.sort_values(by='subject_name').reset_index()

output_df['student_name'] = output_df['student_id'].apply(lambda x: students_df[students_df['student_id'] == x]['student_name'].values[0] if x in students_df['student_id'].values else None)
output_df['subject_name'] = [s for _ in student_dict.keys() for s in subjects_df['subject_name']]
for k, v in student_dict.items():
	subject_list = list(set(v))
	for s in subject_list:
		count = v.count(s)
		#print(f"Student {k} has subject {s} {count} times.")
		output_df.loc[(output_df['student_id'] == k) & (output_df['subject_name'] == s), 'attended_exams'] = count

print(output_df)