class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # 数学的な公式を使用
        return (high + 1) // 2 - low // 2

# 別解（わかりやすい版）
class SolutionAlternative:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2
        # lowまたはhighが奇数なら+1
        if low % 2 == 1 or high % 2 == 1:
            count += 1
        return count

# 最速版（ビット演算）
class SolutionFastest:
    def countOdds(self, low: int, high: int) -> int:
        # ビット演算で奇数判定（& 1）
        return (high - low) // 2 + ((low | high) & 1)

sol = Solution()
sol_alt = SolutionAlternative()
sol_fast = SolutionFastest()

test_cases = [
    (3, 7, 3),      # 3,5,7
    (8, 10, 1),     # 9
    (14, 17, 2),    # 15,17
    (798273637, 970699661, 86213013)
]

for low, high, expected in test_cases:
    result1 = sol.countOdds(low, high)
    result2 = sol_alt.countOdds(low, high)
    result3 = sol_fast.countOdds(low, high)
    
    status = "✅" if result1 == expected else "❌"
    print(f'{status} countOdds({low}, {high}) = {result1} (alt: {result2}, fast: {result3}) expect {expected}')