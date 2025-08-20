class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for idx, n in enumerate(nums):
            n_str = str(n)
            total: int = 0
            for n_ in n_str:
                total += int(n_)
            if total == idx:
                return total
        return -1

sol = Solution()
print(f'{sol.smallestIndex([1,3,2])} expect 2')
print(f'{sol.smallestIndex([1,10,11])} expect 1')