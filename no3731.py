class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        min_val = min(nums)
        max_val = max(nums)
        nums_set = set(nums)
        out_list = []
        for i in range(min_val, max_val + 1):
            if i in nums_set:
                pass
            else:
                out_list.append(i)
        return out_list

sol = Solution()
print(f'{sol.findMissingElements([1,4,2,5])} expect [3]')
print(f'{sol.findMissingElements([7,8,6,9])} expect []')
print(f'{sol.findMissingElements([5,1])} expect [2,3,4]')