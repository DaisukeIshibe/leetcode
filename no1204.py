import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id column contains unique values.
This table has the information about all people waiting for a bus.
The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table.
turn determines the order of which the people will board the bus, where turn=1 denotes the first person to board and turn=n denotes the last person to board.
weight is the weight of the person in kilograms.
 

There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.

Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.

Note that only one person can board the bus at any given turn.
'''
queue = pd.DataFrame({
	'person_id': [5, 4, 3, 6, 1, 2],
	'person_name': ['Alice', 'Bob', 'Alex', 'John Cena', 'Winston', 'Marie'],
	'weight': [250, 175, 350, 400, 500, 200],
	'turn': [1, 5, 2, 3, 6, 4]
})


def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values('turn')
    queue['cumulative_weight'] = queue['weight'].cumsum()
    last_person = queue[queue['cumulative_weight'] <= 1000].iloc[-1]
    return pd.DataFrame({'person_name': [last_person['person_name']]})