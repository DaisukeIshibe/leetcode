class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(nums) % k

sol = Solution()
print(f'{sol.minOperations([3, 9, 7], 5)} expect 4')
print(f'{sol.minOperations([4, 1, 3], 4)} expect 0')
print(f'{sol.minOperations([3, 2], 6)} expect 5')