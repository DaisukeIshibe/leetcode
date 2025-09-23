class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort()
        out_list = []
        for i in range(0, len(nums), 2):
            out_list.append(nums[i + 1])
            out_list.append(nums[i])
        
        return out_list

sol = Solution()
print(f'{sol.numberGame([5,4,2,3])} expect [3,2,5,4]')
print(f'{sol.numberGame([2,5])} expect [5,2]')