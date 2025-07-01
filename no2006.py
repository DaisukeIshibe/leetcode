class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        from itertools import combinations
        count = 0
        for combi_list in combinations(nums, 2):
            abs_diff = abs(combi_list[0] - combi_list[1])
            if k == abs_diff:
                count += 1
        return count


sol = Solution()
nums = [1,2,2,1]
k = 1
print(f'{sol.countKDifference(nums, k)} expect 4') # Output: 4
nums = [1,3]
k = 3
print(f'{sol.countKDifference(nums, k)} expect 0') # Output: 0
nums = [3,2,1,5,4]
k = 2
print(f'{sol.countKDifference(nums, k)} expect 3') # Output: 3