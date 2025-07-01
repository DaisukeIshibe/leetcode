import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
'''
seat_df = pd.DataFrame({
	'id': [1, 2, 3, 4, 5],
	'student': ['Abbot', 'Doris', 'Emerson', 'Green', 'Jeames']
})

def split_list(lst, n):
	k, m = divmod(len(lst), n)
	return [lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]

student_list = seat_df['student'].tolist()
k, m = divmod(len(student_list), 2)
if m == 0:
	n = k
else:
	n = k + 1
s_list = split_list(student_list, n)
print(s_list)
out_list = []
for s in s_list:
	if len(s) == 1:
		out_list.append(s[0])
	else:
		out_list.append(s[-1])
		out_list.append(s[0])

out_df = pd.DataFrame({
	'student': out_list
})