class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        # dp[i][j] = i個の0とj個の1で作れる文字列の最大数
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            # 各文字列の0と1の個数を数える
            zeros = s.count('0')
            ones = s.count('1')
            
            # 逆順でDPテーブルを更新（重複使用を防ぐため）
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    # 現在の文字列を含める場合と含めない場合の最大値
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        
        return dp[m][n]

# 最適化版（メモリ効率改善）
class SolutionOptimized:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        # 文字列の0と1の個数を事前計算
        counts = [(s.count('0'), s.count('1')) for s in strs]
        
        # DPテーブル初期化
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for zeros, ones in counts:
            # 逆順で更新して重複使用を防ぐ
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        
        return dp[m][n]

# 高速版（ビット演算最適化）
class SolutionFast:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        # 1次元DPで空間計算量を削減
        dp = [0] * ((m + 1) * (n + 1))
        
        def get_index(i, j):
            return i * (n + 1) + j
        
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            
            # 新しいDPテーブルを作成
            new_dp = dp[:]
            
            for i in range(zeros, m + 1):
                for j in range(ones, n + 1):
                    curr_idx = get_index(i, j)
                    prev_idx = get_index(i - zeros, j - ones)
                    new_dp[curr_idx] = max(dp[curr_idx], dp[prev_idx] + 1)
            
            dp = new_dp
        
        return dp[get_index(m, n)]

# デバッグ用
def debug_solution(strs, m, n):
    print(f"Input: strs={strs}, m={m}, n={n}")
    
    for i, s in enumerate(strs):
        zeros = s.count('0')
        ones = s.count('1')
        print(f"  String {i}: '{s}' -> 0s: {zeros}, 1s: {ones}")
    
    sol = Solution()
    result = sol.findMaxForm(strs, m, n)
    print(f"Result: {result}\n")
    
    return result

# テスト実行
sol = Solution()
sol_opt = SolutionOptimized()

print("=== 基本版 ===")
print(f'{sol.findMaxForm(["10","0001","111001","1","0"], 5, 3)} expect 4')
print(f'{sol.findMaxForm(["10","0","1"], 1, 1)} expect 2')
print(f'{sol.findMaxForm(["10","0001","111001","1","0"], 4, 3)} expect 3')

print("\n=== 最適化版 ===")
print(f'{sol_opt.findMaxForm(["10","0001","111001","1","0"], 5, 3)} expect 4')
print(f'{sol_opt.findMaxForm(["10","0","1"], 1, 1)} expect 2')
print(f'{sol_opt.findMaxForm(["10","0001","111001","1","0"], 4, 3)} expect 3')

print("\n=== デバッグ情報 ===")
debug_solution(["10","0001","111001","1","0"], 5, 3)
debug_solution(["10","0","1"], 1, 1)