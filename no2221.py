class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        for i in range(len(nums), 0, -1):
            out_list = []
            for j in range(i):
                out_list.append(j)
            print(i, out_list)
        return 0

sol = Solution()
print(f'{sol.triangularSum([1,2,3,4,5])} expect 8')
print(f'{sol.triangularSum([5])} expect 5')