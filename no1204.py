import pandas as pd
'''
Queue table:
+-----------+-------------+--------+------+
| person_id | person_name | weight | turn |
+-----------+-------------+--------+------+
| 5         | Alice       | 250    | 1    |
| 4         | Bob         | 175    | 5    |
| 3         | Alex        | 350    | 2    |
| 6         | John Cena   | 400    | 3    |
| 1         | Winston     | 500    | 6    |
| 2         | Marie       | 200    | 4    |
+-----------+-------------+--------+------+
'''
queue = pd.DataFrame({
	'person_id': [5, 4, 3, 6, 1, 2],
	'person_name': ['Alice', 'Bob', 'Alex', 'John Cena', 'Winston', 'Marie'],
	'weight': [250, 175, 350, 400, 500, 200],
	'turn': [1, 5, 2, 3, 6, 4]
})

# Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.
# Note that only one person can board the bus at any given turn.

def find_last_person(queue: pd.DataFrame, weight_limit: int) -> pd.DataFrame:
    last_person = None
    for _, row in queue.iterrows():
        if weight_limit < row['weight'] * row['turn']:
            last_person = row
    return pd.DataFrame([last_person]) if last_person is not None else pd.DataFrame()

out_df = find_last_person(queue, 1000)
print(out_df)