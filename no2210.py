class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        len_n = len(nums)
        for i in range(1, len_n - 1):
            currnt_n = nums[i]
            before_n = nums[i - 1]
        return 0

sol = Solution()
print(f'{sol.countHillValley([2,4,1,1,6,5])} expect 3')
print(f'{sol.countHillValley([6,6,5,5,4,1])} expect 0')