import pandas as pd
'''
Input
+-----+----------+----------+-----+-----+
| pid | tiv_2015 | tiv_2016 | lat | lon |
+-----+----------+----------+-----+-----+
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
+-----+----------+----------+-----+-----+
Output
+----------+
| tiv_2016 |
+----------+
| 45.00    |
+----------+
'''
# Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:
# have the same tiv_2015 value as one or more other policyholders, and
# are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
# Round tiv_2016 to two decimal places.
insurance = pd.DataFrame({
	'pid': [1, 2, 3, 4],
	'tiv_2015': [10, 20, 10, 10],
	'tiv_2016': [5, 20, 30, 40],
	'lat': [10, 20, 20, 40],
	'lon': [10, 20, 20, 40]
})
# Find tiv_2015 values that are duplicated
duplicated_tiv_2015 = insurance[insurance.duplicated('tiv_2015', keep=False)]['tiv_2015'].unique()
# Find (lat, lon) pairs that are duplicated
duplicated_locations = insurance[insurance.duplicated(['lat', 'lon'], keep=False)][['lat', 'lon']]
# Filter insurance for the conditions
filtered_insurance = insurance[
	(insurance['tiv_2015'].isin(duplicated_tiv_2015)) &
	(~insurance.set_index(['lat', 'lon']).index.isin(duplicated_locations.set_index(['lat', 'lon']).index))
]
# Sum tiv_2016 and round to two decimal places
total_tiv_2016 = round(filtered_insurance['tiv_2016'].sum(), 2)
result = pd.DataFrame({'tiv_2016': [total_tiv_2016]})
print(result)