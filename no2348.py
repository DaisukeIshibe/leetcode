class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        count = 0
        total = 0
        for n in nums:
            if n == 0:
                count += 1
                total += count
            else:
                count = 0
        return total


sol = Solution()
print(f'{sol.zeroFilledSubarray([1,3,0,0,2,0,0,4])} expect 6')
print(f'{sol.zeroFilledSubarray([0,0,0,2,0,0])} expect 9')
print(f'{sol.zeroFilledSubarray([2,10,2019])} expect 0')