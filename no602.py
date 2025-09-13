import pandas as pd
'''
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+
'''
request_accepted = pd.DataFrame({
	'requester_id': [1, 1, 2, 3],
	'accepter_id': [2, 3, 3, 4],
	'accept_date': ['2016/06/03', '2016/06/08', '2016/06/08', '2016/06/09']
})
# Write a solution to find the people who have the most friends and the most friends number.
#The test cases are generated so that only one person has the most friends.
request_accepted = pd.concat([request_accepted[['requester_id', 'accepter_id']].rename(columns={'requester_id': 'id'}),
							   request_accepted[['accepter_id', 'requester_id']].rename(columns={'accepter_id': 'id'})])
friend_count = request_accepted.groupby('id').size().reset_index(name='friend_count')
result = friend_count[friend_count['friend_count'] == friend_count['friend_count'].max()]
# Format the columns: | id | num |
result = result.rename(columns={'friend_count': 'num'})