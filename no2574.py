class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left_list = [0]
        left_sum = 0
        for n in nums:
            left_sum += n
            left_list.append(left_sum)
        left_list.pop(-1)

        right_list = [0]
        right_sum = 0
        rev_nums = reversed(nums)
        for n in rev_nums:
            right_sum += n
            right_list.append(right_sum)
        right_list.pop(-1)
        right_list.reverse()

        return [abs(a - b) for a, b in zip(left_list, right_list)]

sol = Solution()
print(f'{sol.leftRightDifference([10,4,8,3])} expect [15,1,11,22]')
print(f'{sol.leftRightDifference([1])} expect [0]')