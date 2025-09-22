class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_len = 0
        curr = 0
        prev = 0
        found_zero = False

        for n in nums:
            if n == 1:
                curr += 1
            else:
                found_zero = True
                max_len = max(max_len, prev + curr)
                prev = curr
                curr = 0
        max_len = max(max_len, prev + curr)
        return max_len if found_zero else len(nums) - 1


sol = Solution()
print(f'{sol.longestSubarray([1,1,0,1])} expect 3')
print(f'{sol.longestSubarray([0,1,1,1,0,1,1,0,1])} expect 5')
print(f'{sol.longestSubarray([1,1,1])} expect 2')
print(f'{sol.longestSubarray([1,1,0,0,1,0,1,0,0,1])} expect 2')
print(f'{sol.longestSubarray([1,1,0,0,1,1,1,0,1])} expect 4')
print(f'{sol.longestSubarray([0,0,1,1])} expect 2')
print(f'{sol.longestSubarray([1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1])} expect 14')
print(f'{sol.longestSubarray([1,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1])} expect 9')
print(f'{sol.longestSubarray([1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1])} expect 15')
print(f'{sol.longestSubarray([1,1,1,0,1,1,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1])} expect 8')