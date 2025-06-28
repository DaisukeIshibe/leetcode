import pandas as pd
'''
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| product     | object |
| quarter_1   | int    |
| quarter_2   | int    |
| quarter_3   | int    |
| quarter_4   | int    |
+-------------+--------+
+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+
'''
report_df = pd.DataFrame({
	'product': ['Umbrella', 'SleepingBag'],
	'quarter_1': [417, 800],
	'quarter_2': [224, 936],
	'quarter_3': [379, 93],
	'quarter_4': [611, 875]
})

out_df = report_df.melt(id_vars=['product'], var_name='quarter', value_name='sales')
print(out_df)