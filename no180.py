import pandas as pd
'''
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
'''
logs = pd.DataFrame({
	'id': [1, 2, 3, 4, 5, 6, 7],
	'num': [1, 1, 1, 2, 1, 2, 2]
})
#  Find all numbers that appear at least three times consecutively.
logs['consecutive'] = logs['num'].rolling(window=3).apply(lambda x: x.nunique() == 1 and x.count() == 3)
logs = logs.dropna()
# if consecutive number > 0, then extract the frame
out_df = pd.DataFrame(columns=['ConsecutiveNums'])
out_df['ConsecutiveNums'] = logs[logs['consecutive'] > 0]['num'].unique()
print(out_df)