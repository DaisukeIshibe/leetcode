class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        sorted_list = sorted(nums, reverse=True)
        print(sorted_list)
        return 0

sol = Solution()
print(f'{sol.maxSumDivThree([3,6,5,1,8])} expect 18')
print(f'{sol.maxSumDivThree([4])} expect 0')
print(f'{sol.maxSumDivThree([1,2,3,4,4])} expect 12')