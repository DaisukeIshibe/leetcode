class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        import collections
        c = collections.Counter(nums)
        for _, v in c.items():
            if v % 2 == 0:
                pass
            else:
                return False
        return True

sol = Solution()
print(f'{sol.divideArray([3,2,3,2,2,2])} expect True')
print(f'{sol.divideArray([1,2,3,4])} expect False')