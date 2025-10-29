import pandas as pd

# データ
transactions = pd.DataFrame({
    'transaction_id': [1, 2, 3, 4, 5, 6],
    'amount': [150, 200, 75, 300, 50, 120],
    'transaction_date': ['2024-07-01', '2024-07-01', '2024-07-01', '2024-07-02', '2024-07-02', '2024-07-03']
})

# 最も効率的で正確な解法
def sum_odd_even_transactions_correct(transactions: pd.DataFrame) -> pd.DataFrame:
    # 日付を datetime に変換し、奇数偶数フラグを追加
    df = transactions.assign(
        transaction_date=pd.to_datetime(transactions['transaction_date']),
        is_odd=transactions['transaction_id'] % 2
    )
    
    # pivot_table で効率的に集計
    result = (df.pivot_table(
        index='transaction_date',
        columns='is_odd',
        values='amount',
        aggfunc='sum',
        fill_value=0
    ).reset_index())
    
    # 列名を設定（0=偶数, 1=奇数）
    result.columns = ['transaction_date', 'even_sum', 'odd_sum']
    
    # 列順序を調整
    return result[['transaction_date', 'odd_sum', 'even_sum']].sort_values('transaction_date').reset_index(drop=True)

# より高速なベクトル化版
def sum_odd_even_transactions_vectorized(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.assign(
        transaction_date=pd.to_datetime(transactions['transaction_date']),
        odd_amount=lambda x: x['amount'] * (x['transaction_id'] % 2),
        even_amount=lambda x: x['amount'] * (1 - x['transaction_id'] % 2)
    )
    
    return (df.groupby('transaction_date', as_index=False)
            .agg({'odd_amount': 'sum', 'even_amount': 'sum'})
            .rename(columns={'odd_amount': 'odd_sum', 'even_amount': 'even_sum'})
            [['transaction_date', 'odd_sum', 'even_sum']])

# 最高速版（NumPy風）
def sum_odd_even_transactions_numpy_style(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.copy()
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    
    # マスクを使った高速計算
    odd_mask = df['transaction_id'] % 2 == 1
    df['odd_amount'] = df['amount'].where(odd_mask, 0)
    df['even_amount'] = df['amount'].where(~odd_mask, 0)
    
    return (df.groupby('transaction_date', as_index=False)
            [['odd_amount', 'even_amount']]
            .sum()
            .rename(columns={'odd_amount': 'odd_sum', 'even_amount': 'even_sum'}))

# デバッグ用：詳細確認
def debug_transactions(transactions: pd.DataFrame):
    print("=== デバッグ情報 ===")
    df = transactions.copy()
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df['is_odd'] = df['transaction_id'] % 2
    df['parity'] = df['transaction_id'].apply(lambda x: 'odd' if x % 2 == 1 else 'even')
    
    print("詳細データ:")
    print(df[['transaction_id', 'amount', 'transaction_date', 'parity']])
    print()
    
    for date, group in df.groupby('transaction_date'):
        print(f"日付: {date.date()}")
        odd_transactions = group[group['is_odd'] == 1]
        even_transactions = group[group['is_odd'] == 0]
        
        print(f"  奇数ID取引: {list(odd_transactions['transaction_id'])} → 合計: {odd_transactions['amount'].sum()}")
        print(f"  偶数ID取引: {list(even_transactions['transaction_id'])} → 合計: {even_transactions['amount'].sum()}")
        print()

# 実行と結果確認
print("=== デバッグ実行 ===")
debug_transactions(transactions)

print("=== 正しい結果 ===")
result_correct = sum_odd_even_transactions_correct(transactions)
print(result_correct)
print()

print("=== ベクトル化版 ===")
result_vectorized = sum_odd_even_transactions_vectorized(transactions)
print(result_vectorized)
print()

print("=== NumPy風版 ===")
result_numpy = sum_odd_even_transactions_numpy_style(transactions)
print(result_numpy)

# 正しい期待される出力
print("\n=== 正しい期待される出力 ===")
correct_expected = pd.DataFrame({
    'transaction_date': pd.to_datetime(['2024-07-01', '2024-07-02', '2024-07-03']),
    'odd_sum': [225, 50, 0],      # 修正: 150+75=225, 50, 0
    'even_sum': [200, 300, 120]   # 修正: 200, 300, 120
})
print(correct_expected)