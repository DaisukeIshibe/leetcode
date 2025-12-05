class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return -1
        sorted_list = sorted(nums)
        return sorted_list[1]

sol = Solution()
print(f'{sol.findNonMinOrMax([3,2,1,4])} expect 2 or 3')
print(f'{sol.findNonMinOrMax([1,2])} expect -1')
print(f'{sol.findNonMinOrMax([2,1,3])} expect 2')