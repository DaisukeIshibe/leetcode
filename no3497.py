import pandas as pd

user_activity = pd.DataFrame({
    'user_id': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4],
    'activity_date': ['2023-01-01', '2023-01-02', '2023-01-05', '2023-01-10', '2023-01-12', '2023-01-15',
                      '2023-02-01', '2023-02-03', '2023-02-07', '2023-02-10',
                      '2023-03-05', '2023-03-06', '2023-03-08', '2023-03-12', '2023-03-15', '2023-03-20',
                      '2023-04-01', '2023-04-03', '2023-04-05', '2023-04-07'],
    'activity_type': ['free_trial', 'free_trial', 'free_trial', 'paid', 'paid', 'paid',
                      'free_trial', 'free_trial', 'free_trial', 'cancelled',
                      'free_trial', 'free_trial', 'free_trial', 'paid', 'paid', 'paid',
                      'free_trial', 'free_trial', 'paid', 'cancelled'],
    'activity_duration': [45, 30, 60, 75, 90, 65, 55, 25, 50, 0,
                         70, 60, 80, 50, 55, 85, 40, 35, 45, 0]
})

# 方法1: 元のコードの修正版（最小限の変更）
def solution_basic():
    user_activity['activity_date'] = pd.to_datetime(user_activity['activity_date'])
    # 修正: unique() に括弧を追加
    converted_users = user_activity[user_activity['activity_type'] == 'paid']['user_id'].unique()
    converted_data = user_activity[user_activity['user_id'].isin(converted_users)]
    
    trial_avg = converted_data[converted_data['activity_type'] == 'free_trial'].groupby('user_id')['activity_duration'].mean().reset_index()
    paid_avg = converted_data[converted_data['activity_type'] == 'paid'].groupby('user_id')['activity_duration'].mean().reset_index()
    # trial_avg と paid_avg を小数点第2位で四捨五入する。roundを使わないで四捨五入する。
    trial_avg['activity_duration'] = trial_avg['activity_duration'].apply(lambda x: int(x * 100 + 0.5) / 100)
    paid_avg['activity_duration'] = paid_avg['activity_duration'].apply(lambda x: int(x * 100 + 0.5) / 100)

    result = trial_avg.merge(paid_avg, on='user_id', suffixes=('_trial', '_paid'))
    result.columns = ['user_id', 'trial_avg_duration', 'paid_avg_duration']
    return result.sort_values(by='user_id').reset_index(drop=True)

# 方法2: 最適化版（推奨）
def solution_optimized():
    # 1パスで両方の平均を計算
    result = (user_activity
              .query("activity_type in ['free_trial', 'paid']")  # cancelledを除外
              .groupby(['user_id', 'activity_type'])['activity_duration']
              .mean()
              .unstack(fill_value=0)  # free_trial と paid を列に展開
              .round(2)
              .reset_index())
    
    # paid がある（値が0でない）ユーザーのみフィルター
    result = result[result['paid'] > 0]
    
    # 列名を変更
    result.columns = ['user_id', 'trial_avg_duration', 'paid_avg_duration']
    
    return result.sort_values('user_id').reset_index(drop=True)

# 方法3: 最も高速な版（pivot_table使用）
def solution_fastest():
    # pivot_tableで一度に集計
    pivot = (user_activity
             .query("activity_type in ['free_trial', 'paid']")
             .pivot_table(
                 index='user_id',
                 columns='activity_type', 
                 values='activity_duration',
                 aggfunc='mean'
             )
             .round(2)
             .reset_index())
    
    # paidがあるユーザーのみ（NaNでない）
    pivot = pivot.dropna(subset=['paid'])
    
    # 列名を設定
    pivot.columns = ['user_id', 'trial_avg_duration', 'paid_avg_duration']
    
    return pivot.sort_values('user_id').reset_index(drop=True)

# 方法4: 最も堅牢で効率的な版
def solution_robust():
    # 有料プランに転換したユーザーを特定
    paid_users = set(user_activity.query("activity_type == 'paid'")['user_id'])
    
    # 転換ユーザーのデータのみフィルター
    converted_data = user_activity[user_activity['user_id'].isin(paid_users)]
    
    # 各活動タイプの平均を計算
    averages = (converted_data
                .query("activity_type in ['free_trial', 'paid']")
                .groupby(['user_id', 'activity_type'])['activity_duration']
                .mean()
                .unstack()
                .round(2)
                .reset_index())
    
    # 列名を設定
    averages.columns = ['user_id', 'trial_avg_duration', 'paid_avg_duration']
    
    return averages.sort_values('user_id').reset_index(drop=True)

# 実行と結果表示
print("=== 基本修正版 ===")
print(solution_basic())

print("\n=== 最適化版（推奨） ===")
print(solution_optimized())

print("\n=== 最高速版 ===")
print(solution_fastest())

print("\n=== 堅牢版 ===")
print(solution_robust())