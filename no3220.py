import pandas as pd
'''
Table: transactions

+------------------+------+
| Column Name      | Type | 
+------------------+------+
| transaction_id   | int  |
| amount           | int  |
| transaction_date | date |
+------------------+------+
The transactions_id column uniquely identifies each row in this table.
Each row of this table contains the transaction id, amount and transaction date.
Write a solution to find the sum of amounts for odd and even transactions for each day. If there are no odd or even transactions for a specific date, display as 0.

Return the result table ordered by transaction_date in ascending order.

The result format is in the following example.

 

Example:

Input:

transactions table:

+----------------+--------+------------------+
| transaction_id | amount | transaction_date |
+----------------+--------+------------------+
| 1              | 150    | 2024-07-01       |
| 2              | 200    | 2024-07-01       |
| 3              | 75     | 2024-07-01       |
| 4              | 300    | 2024-07-02       |
| 5              | 50     | 2024-07-02       |
| 6              | 120    | 2024-07-03       |
+----------------+--------+------------------+
  
Output:

+------------------+---------+----------+
| transaction_date | odd_sum | even_sum |
+------------------+---------+----------+
| 2024-07-01       | 75      | 350      |
| 2024-07-02       | 0       | 350      |
| 2024-07-03       | 0       | 120      |
+------------------+---------+----------+
'''
transactions = pd.DataFrame({
    'transaction_id': [1, 2, 3, 4, 5, 6],
    'amount': [150, 200, 75, 300, 50, 120],
    'transaction_date': ['2024-07-01', '2024-07-01', '2024-07-01', '2024-07-02', '2024-07-02', '2024-07-03']
})

# 方法1: 元のコードの修正版
def sum_daily_odd_even_fixed(transactions: pd.DataFrame) -> pd.DataFrame:
    # amountが奇数か偶数かで判定（修正点）
    transactions = transactions.copy()
    transactions['is_odd'] = transactions['amount'] % 2 != 0
    
    result = transactions.groupby('transaction_date').apply(
        lambda x: pd.Series({
            'odd_sum': x.loc[x['is_odd'], 'amount'].sum(),
            'even_sum': x.loc[~x['is_odd'], 'amount'].sum()
        })
    ).reset_index()
    
    result['odd_sum'] = result['odd_sum'].fillna(0).astype(int)
    result['even_sum'] = result['even_sum'].fillna(0).astype(int)
    
    return result.sort_values(by='transaction_date').reset_index(drop=True)

# 方法2: 最適化版（推奨）
def sum_daily_odd_even_optimized(transactions: pd.DataFrame) -> pd.DataFrame:
    # amountの奇数偶数で分類
    df = transactions.assign(
        transaction_date=pd.to_datetime(transactions['transaction_date']),
        is_odd=transactions['amount'] % 2
    )
    
    # pivot_tableで効率的に集計
    result = (df.pivot_table(
        index='transaction_date',
        columns='is_odd',
        values='amount',
        aggfunc='sum',
        fill_value=0
    ).reset_index())
    
    # 列名を設定（0=偶数, 1=奇数）
    result.columns = ['transaction_date', 'even_sum', 'odd_sum']
    
    return result[['transaction_date', 'odd_sum', 'even_sum']].sort_values('transaction_date').reset_index(drop=True)

# 方法3: 最高速ベクトル化版
def sum_daily_odd_even_vectorized(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.assign(
        transaction_date=pd.to_datetime(transactions['transaction_date']),
        odd_amount=lambda x: x['amount'] * (x['amount'] % 2),
        even_amount=lambda x: x['amount'] * (1 - x['amount'] % 2)
    )
    
    return (df.groupby('transaction_date', as_index=False)
            .agg({'odd_amount': 'sum', 'even_amount': 'sum'})
            .rename(columns={'odd_amount': 'odd_sum', 'even_amount': 'even_sum'})
            [['transaction_date', 'odd_sum', 'even_sum']])

# 方法4: マスクを使った高速版
def sum_daily_odd_even_mask(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.copy()
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    
    # マスクを使った高速計算
    odd_mask = df['amount'] % 2 == 1
    df['odd_amount'] = df['amount'].where(odd_mask, 0)
    df['even_amount'] = df['amount'].where(~odd_mask, 0)
    
    return (df.groupby('transaction_date', as_index=False)
            [['odd_amount', 'even_amount']]
            .sum()
            .rename(columns={'odd_amount': 'odd_sum', 'even_amount': 'even_sum'}))

# デバッグ用：詳細確認
def debug_amount_parity(transactions: pd.DataFrame):
    print("=== Amount の奇数偶数判定 ===")
    df = transactions.copy()
    df['amount_parity'] = df['amount'].apply(lambda x: 'odd' if x % 2 == 1 else 'even')
    
    print("詳細データ:")
    print(df[['transaction_id', 'amount', 'transaction_date', 'amount_parity']])
    print()
    
    for date, group in df.groupby('transaction_date'):
        print(f"日付: {date}")
        odd_amounts = group[group['amount'] % 2 == 1]
        even_amounts = group[group['amount'] % 2 == 0]
        
        print(f"  奇数amount: {list(odd_amounts['amount'])} → 合計: {odd_amounts['amount'].sum()}")
        print(f"  偶数amount: {list(even_amounts['amount'])} → 合計: {even_amounts['amount'].sum()}")
        print()

# 実行と結果確認
print("=== デバッグ実行 ===")
debug_amount_parity(transactions)

print("=== 修正版結果 ===")
result1 = sum_daily_odd_even_fixed(transactions)
print(result1)
print()

print("=== 最適化版結果 ===")
result2 = sum_daily_odd_even_optimized(transactions)
print(result2)
print()

print("=== ベクトル化版結果 ===")
result3 = sum_daily_odd_even_vectorized(transactions)
print(result3)
print()

print("=== 期待される出力 ===")
expected = pd.DataFrame({
    'transaction_date': pd.to_datetime(['2024-07-01', '2024-07-02', '2024-07-03']),
    'odd_sum': [75, 0, 0],       # 75のみが奇数
    'even_sum': [350, 350, 120]  # 150+200=350, 300+50=350, 120
})
print(expected)