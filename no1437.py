class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_one_index = -1
        
        for i, num in enumerate(nums):
            if num == 1:
                if last_one_index != -1:  # 前に1があった場合
                    if i - last_one_index - 1 < k:  # 間の0の数がk未満
                        return False
                last_one_index = i
        
        return True

# より簡潔な版
class SolutionConcise:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        prev = -k - 1  # 初期値を設定（最初の1との距離がk以上になるように）
        
        for i, num in enumerate(nums):
            if num == 1:
                if i - prev <= k:
                    return False
                prev = i
        
        return True

# デバッグ用詳細版
class SolutionDebug:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        print(f"Input: nums={nums}, k={k}")
        
        ones_positions = [i for i, num in enumerate(nums) if num == 1]
        print(f"Positions of 1s: {ones_positions}")
        
        for i in range(1, len(ones_positions)):
            distance = ones_positions[i] - ones_positions[i-1] - 1
            print(f"Distance between positions {ones_positions[i-1]} and {ones_positions[i]}: {distance}")
            
            if distance < k:
                print(f"Distance {distance} < k={k}, returning False")
                return False
        
        print("All distances are valid, returning True")
        return True

# 正規表現を使った版
class SolutionRegex:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        import re
        s = ''.join(map(str, nums))
        
        # 1の間にk個未満の0がある場合を検出
        pattern = f'1[0]{{{0},{k-1}}}1' if k > 0 else '11'
        
        return not bool(re.search(pattern, s))

# テスト実行
sol = Solution()
sol_concise = SolutionConcise()
sol_debug = SolutionDebug()

print("=== 修正版結果 ===")
test_cases = [
    ([1,0,0,0,1,0,0,1], 2),
    ([1,0,0,1,0,1], 2), 
    ([1,0,0,0,1,0,0,1,0], 2),
    ([1,1], 1),
    ([0,1,0,1], 1),
    ([1], 0),
    ([0,0,0], 1)
]

for nums, k in test_cases:
    result = sol.kLengthApart(nums, k)
    result_concise = sol_concise.kLengthApart(nums, k)
    print(f"nums={nums}, k={k} -> {result} (concise: {result_concise})")

print("\n=== デバッグ詳細 ===")
print("Test case: [1,0,0,0,1,0,0,1,0], k=2")
sol_debug.kLengthApart([1,0,0,0,1,0,0,1,0], 2)