import pandas as pd
'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| revenue     | int     |
| month       | varchar |
+-------------+---------+
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+
'''
department = pd.DataFrame({
	'id': [1, 2, 3, 1, 1],
	'revenue': [8000, 9000, 10000, 7000, 6000],
	'month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar']
})

# Reformat the table such that there is a department id column and a revenue column for each month.
# Output sample is as follows:
# +------+-------------+-------------+-------------+-----+-------------+
# | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
# +------+-------------+-------------+-------------+-----+-------------+
# | 1    | 8000        | 7000        | 6000        | ... | null        |
# | 2    | 9000        | null        | null        | ... | null        |
# | 3    | null        | 10000       | null        | ... | null        |
# +------+-------------+-------------+-------------+-----+-------------+
result = department.pivot_table(index='id', columns='month', values='revenue', aggfunc='sum').reset_index()
result.columns = ['id'] + [f"{month}_Revenue" for month in result.columns if month != 'id']
# Ensure all months are present in the final output
for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
    if f"{month}_Revenue" not in result.columns:
        result[f"{month}_Revenue"] = None
result = result[['id', 'Jan_Revenue', 'Feb_Revenue', 'Mar_Revenue', 'Apr_Revenue', 'May_Revenue', 'Jun_Revenue', 'Jul_Revenue', 'Aug_Revenue', 'Sep_Revenue', 'Oct_Revenue', 'Nov_Revenue', 'Dec_Revenue']]
print(result)