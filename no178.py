import pandas as pd
'''
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
'''
# Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:
# The scores should be ranked from the highest to the lowest.
# If there is a tie between two scores, both should have the same ranking.
# After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
# Return the result table ordered by score in descending order.

score = pd.DataFrame({
	'id': [1, 2, 3, 4, 5, 6],
	'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
})

# Use rank method with 'dense' method to handle ties and rank from highest to lowest
score['rank'] = score['score'].rank(method='dense', ascending=False).astype(int)
result = score.sort_values(by='score', ascending=False).reset_index(drop=True)
# Eliminate the 'id' column as it's not needed in the output
result = result[['score', 'rank']]
print(result)