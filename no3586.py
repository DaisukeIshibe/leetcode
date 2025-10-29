import pandas as pd
'''
Table: patients

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| patient_id  | int     |
| patient_name| varchar |
| age         | int     |
+-------------+---------+
patient_id is the unique identifier for this table.
Each row contains information about a patient.
Table: covid_tests

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| test_id     | int     |
| patient_id  | int     |
| test_date   | date    |
| result      | varchar |
+-------------+---------+
test_id is the unique identifier for this table.
Each row represents a COVID test result. The result can be Positive, Negative, or Inconclusive.
Write a solution to find patients who have recovered from COVID - patients who tested positive but later tested negative.

A patient is considered recovered if they have at least one Positive test followed by at least one Negative test on a later date
Calculate the recovery time in days as the difference between the first positive test and the first negative test after that positive test
Only include patients who have both positive and negative test results
Return the result table ordered by recovery_time in ascending order, then by patient_name in ascending order.

The result format is in the following example.

 

Example:

Input:

patients table:

+------------+--------------+-----+
| patient_id | patient_name | age |
+------------+--------------+-----+
| 1          | Alice Smith  | 28  |
| 2          | Bob Johnson  | 35  |
| 3          | Carol Davis  | 42  |
| 4          | David Wilson | 31  |
| 5          | Emma Brown   | 29  |
+------------+--------------+-----+
covid_tests table:

+---------+------------+------------+--------------+
| test_id | patient_id | test_date  | result       |
+---------+------------+------------+--------------+
| 1       | 1          | 2023-01-15 | Positive     |
| 2       | 1          | 2023-01-25 | Negative     |
| 3       | 2          | 2023-02-01 | Positive     |
| 4       | 2          | 2023-02-05 | Inconclusive |
| 5       | 2          | 2023-02-12 | Negative     |
| 6       | 3          | 2023-01-20 | Negative     |
| 7       | 3          | 2023-02-10 | Positive     |
| 8       | 3          | 2023-02-20 | Negative     |
| 9       | 4          | 2023-01-10 | Positive     |
| 10      | 4          | 2023-01-18 | Positive     |
| 11      | 5          | 2023-02-15 | Negative     |
| 12      | 5          | 2023-02-20 | Negative     |
+---------+------------+------------+--------------+
Output:

+------------+--------------+-----+---------------+
| patient_id | patient_name | age | recovery_time |
+------------+--------------+-----+---------------+
| 1          | Alice Smith  | 28  | 10            |
| 3          | Carol Davis  | 42  | 10            |
| 2          | Bob Johnson  | 35  | 11            |
+------------+--------------+-----+---------------+
Explanation:

Alice Smith (patient_id = 1):
First positive test: 2023-01-15
First negative test after positive: 2023-01-25
Recovery time: 25 - 15 = 10 days
Bob Johnson (patient_id = 2):
First positive test: 2023-02-01
Inconclusive test on 2023-02-05 (ignored for recovery calculation)
First negative test after positive: 2023-02-12
Recovery time: 12 - 1 = 11 days
Carol Davis (patient_id = 3):
Had negative test on 2023-01-20 (before positive test)
First positive test: 2023-02-10
First negative test after positive: 2023-02-20
Recovery time: 20 - 10 = 10 days
Patients not included:
David Wilson (patient_id = 4): Only has positive tests, no negative test after positive
Emma Brown (patient_id = 5): Only has negative tests, never tested positive
Output table is ordered by recovery_time in ascending order, and then by patient_name in ascending order.
'''
patients = pd.DataFrame({
	'patient_id': [1, 2, 3, 4, 5],
	'patient_name': ['Alice Smith', 'Bob Johnson', 'Carol Davis', 'David Wilson', 'Emma Brown'],
	'age': [28, 35, 42, 31, 29]
})

covid_tests = pd.DataFrame({
	'test_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
	'patient_id': [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5],
	'test_date': ['2023-01-15', '2023-01-25', '2023-02-01', '2023-02-05', '2023-02-12',
				  '2023-01-20', '2023-02-10', '2023-02-20', '2023-01-10', '2023-01-18',
				  '2023-02-15', '2023-02-20'],
	'result': ['Positive', 'Negative', 'Positive', 'Inconclusive', 'Negative',
			   'Negative', 'Positive', 'Negative', 'Positive', 'Positive', 'Negative', 'Negative']
})

# Convert test_date to datetime
covid_tests['test_date'] = pd.to_datetime(covid_tests['test_date'])
# Merge patients with their covid tests
merged = patients.merge(covid_tests, on='patient_id', how='inner')
# Initialize a list to store recovery data
recovery_data = []
# Iterate through each patient to find recovery time
for patient_id, group in merged.groupby('patient_id'):
	positive_tests = group[group['result'] == 'Positive'].sort_values('test_date')
	negative_tests = group[group['result'] == 'Negative'].sort_values('test_date')
	if not positive_tests.empty and not negative_tests.empty:
		first_positive_date = positive_tests.iloc[0]['test_date']
		subsequent_negatives = negative_tests[negative_tests['test_date'] > first_positive_date]
		if not subsequent_negatives.empty:
			first_negative_date = subsequent_negatives.iloc[0]['test_date']
			recovery_time = (first_negative_date - first_positive_date).days
			patient_info = group.iloc[0][['patient_id', 'patient_name', 'age']]
			recovery_data.append({
				'patient_id': patient_info['patient_id'],
				'patient_name': patient_info['patient_name'],
				'age': patient_info['age'],
				'recovery_time': recovery_time
			})
# Create result DataFrame
result = pd.DataFrame(recovery_data)
# Sort the result by recovery_time and patient_name
result = result.sort_values(by=['recovery_time', 'patient_name']).reset_index(drop=True)
print(result)