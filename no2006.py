class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        from itertools import combinations

        for combi_list in combinations(nums, k):
            pass
        return


sol = Solution()
nums = [1,2,2,1]
k = 1
print(sol.countKDifference(nums, k)) # Output: 4
nums = [1,3]
k = 3
print(sol.countKDifference(nums, k)) # Output: 0
nums = [3,2,1,5,4]
k = 2
print(sol.countKDifference(nums, k)) # Output: 3