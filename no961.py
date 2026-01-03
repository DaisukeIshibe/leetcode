class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        n_dict = {}
        for n in nums:
            if n in n_dict:
                return n
            else:
                n_dict[n] = False
        return 0

sol = Solution()
print(f'{sol.repeatedNTimes([1,2,3,3])} expect 3')
print(f'{sol.repeatedNTimes([2,1,2,5,3,2])} expect 2')
print(f'{sol.repeatedNTimes([5,1,5,2,5,3,5,4])} expect 5')