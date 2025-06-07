import pandas as pd

'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| user_name   | varchar |
+-------------+---------+
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| contest_id  | int     |
| user_id     | int     |
+-------------+---------+

+---------+-----------+
| user_id | user_name |
+---------+-----------+
| 6       | Alice     |
| 2       | Bob       |
| 7       | Alex      |
+---------+-----------+
+------------+---------+
| contest_id | user_id |
+------------+---------+
| 215        | 6       |
| 209        | 2       |
| 208        | 2       |
| 210        | 6       |
| 208        | 6       |
| 209        | 7       |
| 209        | 6       |
| 215        | 7       |
| 208        | 7       |
| 210        | 2       |
| 207        | 2       |
| 210        | 7       |
+------------+---------+
'''
register_df = pd.DataFrame({
	'user_id': [6, 2, 7],
	'user_name': ['Alice', 'Bob', 'Alex']
})
contest_df = pd.DataFrame({
	'contest_id': [215, 209, 208, 210, 208, 209, 209, 215, 208, 210, 207, 210],
	'user_id': [6, 2, 2, 6, 6, 7, 6, 7, 7, 2, 2, 7]
})

contest_list = list(set(contest_df['contest_id']))
contest_dict = {c:[] for c in contest_list}

for c, u in zip(contest_df['contest_id'], contest_df['user_id']):
	contest_dict[c].append(u)

user_num = register_df.shape[0]
out_df = pd.DataFrame(columns=['contest_id', 'percentage'])
out_df['contest_id'] = contest_list
out_df['percentage'] = list(map(lambda x: len(set(x)) / user_num * 100, contest_dict.values()))
out_df['percentage'] = out_df['percentage'].round(2)
#out_df = out_df.sort_values('percentage', ascending=False)
# Sort the contest_id by descending order of percentage, and then by ascending order of contest_id
out_df = out_df.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])
print(out_df)