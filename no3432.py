class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        count_diff:int = 0
        for i in range(len(nums) - 1):
            left_list = nums[0:i+1]
            right_list = nums[i+1:]
            sum_left = sum(left_list)
            sum_right = sum(right_list)
            diff = sum_left - sum_right
            if diff % 2 == 0:
                count_diff += 1

        return count_diff

sol = Solution()
print(f'{sol.countPartitions([10,10,3,7,6])} expect 4')
print(f'{sol.countPartitions([1,2,2])} expect 0')
print(f'{sol.countPartitions([2,4,6,8])} expect 3')