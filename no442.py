class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        n_dict = {}
        for n in nums:
            if not n in n_dict:
                n_dict[n] = 1
            else:
                n_dict[n] += 1
        
        return sorted([k for k, v in n_dict.items() if v >= 2])


sol = Solution()
print(f'{sol.findDuplicates([4,3,2,7,8,2,3,1])} expect=[2,3]')
print(f'{sol.findDuplicates([1,1,2])} expect=[1]')