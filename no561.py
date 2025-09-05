class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        # 偶数番目の要素だけ合計することで高速化
        return sum(nums[::2])

sol = Solution()
print(f'{sol.arrayPairSum([1,4,3,2])} expect 4')
print(f'{sol.arrayPairSum([6,2,6,5,1,2])} expect 9')