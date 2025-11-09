class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [idx for idx, n in enumerate(sorted(nums)) if n == target]

sol = Solution()
print(f'{sol.targetIndices([1,2,5,2,3], 2)} [1, 2]')
print(f'{sol.targetIndices([1,2,5,2,3], 3)} [3]')
print(f'{sol.targetIndices([1,2,5,2,3], 5)} [4]')