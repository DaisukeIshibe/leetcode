import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
+-------------+-------------+-------------+
| actor_id    | director_id | timestamp   |
+-------------+-------------+-------------+
| 1           | 1           | 0           |
| 1           | 1           | 1           |
| 1           | 1           | 2           |
| 1           | 2           | 3           |
| 1           | 2           | 4           |
| 2           | 1           | 5           |
| 2           | 1           | 6           |
+-------------+-------------+-------------+
'''
actor_director_df = pd.DataFrame({
	'actor_id': [1, 1, 1, 1, 1, 2, 2],
	'director_id': [1, 1, 1, 2, 2, 1, 1],
	'timestamp': [0, 1, 2, 3, 4, 5, 6]
})

actor_list = actor_director_df['actor_id'].unique().tolist()
out_actor_list = []
out_director_list = []
for actor in actor_list:
	# Get the director_id for the current actor
	director_list = actor_director_df[actor_director_df['actor_id'] == actor]['director_id'].unique().tolist()
	
	for director in director_list:
		cooperated_count = actor_director_df[(actor_director_df['actor_id'] == actor) & 
			(actor_director_df['director_id'] == director)].shape[0]
		if cooperated_count >= 3:
			out_actor_list.append(actor)
			out_director_list.append(director)

out_df = pd.DataFrame({
	'actor_id': out_actor_list,
	'director_id': out_director_list
})
print(out_df)