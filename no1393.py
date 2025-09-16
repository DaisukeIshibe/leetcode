import pandas as pd
'''
+---------------+-----------+---------------+--------+
| stock_name    | operation | operation_day | price  |
+---------------+-----------+---------------+--------+
| Leetcode      | Buy       | 1             | 1000   |
| Corona Masks  | Buy       | 2             | 10     |
| Leetcode      | Sell      | 5             | 9000   |
| Handbags      | Buy       | 17            | 30000  |
| Corona Masks  | Sell      | 3             | 1010   |
| Corona Masks  | Buy       | 4             | 1000   |
| Corona Masks  | Sell      | 5             | 500    |
| Corona Masks  | Buy       | 6             | 1000   |
| Handbags      | Sell      | 29            | 7000   |
| Corona Masks  | Sell      | 10            | 10000  |
'''

stocks = pd.DataFrame({
    'stock_name': ['Leetcode', 'Corona Masks', 'Leetcode', 'Handbags', 'Corona Masks', 'Corona Masks', 'Corona Masks', 'Handbags', 'Corona Masks'],
    'operation': ['Buy', 'Buy', 'Sell', 'Buy', 'Sell', 'Buy', 'Sell', 'Sell', 'Sell'],
    'operation_day': [1, 2, 5, 17, 3, 4, 5, 29, 10],
    'price': [1000, 10, 9000, 30000, 1010, 1000, 500, 7000, 10000]
})

# Convert operation_day to datetime for proper sorting
stocks = stocks.sort_values(by=['stock_name', 'operation_day'])
stocks['operation_day'] = pd.to_datetime(stocks['operation_day'], format='%d')

# 結果をリストで保持し、最後にDataFrame化
results = []
for stock in stocks['stock_name'].unique():
    stock_data = stocks[stocks['stock_name'] == stock]
    buy_prices = []
    total_gain_loss = 0

    for _, row in stock_data.iterrows():
        if row['operation'] == 'Buy':
            buy_prices.append(row['price'])
        elif row['operation'] == 'Sell' and buy_prices:
            buy_price = buy_prices.pop(0)  # FIFO
            total_gain_loss += (row['price'] - buy_price)

    results.append({'stock_name': stock, 'capital_gain_loss': total_gain_loss})

# DataFrame化してソート
result_df = pd.DataFrame(results).sort_values(by='stock_name').reset_index(drop=True)
print(result_df)