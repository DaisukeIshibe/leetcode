import pandas as pd
'''
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| city        | object |
| month       | object |
| temperature | int    |
+-------------+--------+
+--------------+----------+-------------+
| city         | month    | temperature |
+--------------+----------+-------------+
| Jacksonville | January  | 13          |
| Jacksonville | February | 23          |
| Jacksonville | March    | 38          |
| Jacksonville | April    | 5           |
| Jacksonville | May      | 34          |
| ElPaso       | January  | 20          |
| ElPaso       | February | 6           |
| ElPaso       | March    | 26          |
| ElPaso       | April    | 2           |
| ElPaso       | May      | 43          |
+--------------+----------+-------------+
'''
weather_df = pd.DataFrame({
	'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville',
	         'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
	'month': ['January', 'February', 'March', 'April', 'May',
	           'January', 'February', 'March', 'April', 'May'],
	'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
})

pivot_df = weather_df.pivot_table(index='month', 
								   columns='city', 
								   values='temperature', 
								   )
print(pivot_df)