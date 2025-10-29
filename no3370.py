class Solution:
    def smallestNumber(self, n: int) -> int:
        import math
        n_log2 = math.log2(n)
        n_log2_int = int(n_log2)
        base = n_log2_int
        if (n_log2 - n_log2_int) >= 0:
            base += 1
        #print(f'{n_log2_int} {base}')
        return int(math.pow(2, base) - 1)

sol = Solution()
print(f'{sol.smallestNumber(5)} expect 7')
print(f'{sol.smallestNumber(10)} expect 15')
print(f'{sol.smallestNumber(1)} expect 1')
print(f'{sol.smallestNumber(4)} expect 7')