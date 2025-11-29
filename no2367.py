class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # 正の値のユニークな個数が答え
        return len(set(n for n in nums if n > 0))

# 別の効率的な書き方
class SolutionAlternative:
    def minimumOperations(self, nums: list[int]) -> int:
        # 0を除外してユニークな値を数える
        return len({n for n in nums if n})

# setを使わない版（メモリ効率重視）
class SolutionNoSet:
    def minimumOperations(self, nums: list[int]) -> int:
        # ソートして連続する異なる値を数える
        sorted_nums = sorted(n for n in nums if n > 0)
        if not sorted_nums:
            return 0
        
        count = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] != sorted_nums[i-1]:
                count += 1
        return count

sol = Solution()
print(f'{sol.minimumOperations([1,5,0,3,5])} expect 3')
print(f'{sol.minimumOperations([0])} expect 0')