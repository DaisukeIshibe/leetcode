class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        n_list = sorted([(n, idx) for idx, n in enumerate(nums)], key=lambda x:x[0])
        return [v for v, _ in sorted(n_list[len(nums) - k:], key=lambda x:x[1])]

sol = Solution()
print(f'{sol.maxSubsequence([2,1,3,3], 2)} expect [3, 3]')
print(f'{sol.maxSubsequence([-1,-2,3,4], 3)} expect [-1 3 4]')
print(f'{sol.maxSubsequence([3,4,3,3], 2)} expect [3, 4] or [4, 3]')
print(f'{sol.maxSubsequence([50,-75], 2)} expect [50, -75]')