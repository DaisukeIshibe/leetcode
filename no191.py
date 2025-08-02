class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for c in str(bin(n))[2:]:
            total += int(c)
        return total

sol = Solution()
print(f'{sol.hammingWeight(11)} expect 3')
print(f'{sol.hammingWeight(128)} expect 1')
print(f'{sol.hammingWeight(2147483645)} expect 30')