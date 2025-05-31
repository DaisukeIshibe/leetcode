import pandas as pd
'''
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+

+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
+------------+--------------+--------------+
'''
patient_df = pd.DataFrame({
	'patient_id': [1, 2, 3, 4, 5],
	'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
	'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201']
})

# Find patients with conditions starting with 'DIAB1'
out_df = patient_df[patient_df['conditions'].apply(lambda x: any(w.startswith('DIAB1') for w in x.split()))]
out_df = out_df[['patient_id', 'patient_name']].reset_index(drop=True)
print(out_df)