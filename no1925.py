class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n+1):
            for b in range(a, n+1):
                c2 = a*a + b*b
                c = int(c2**0.5)
                if c <= n and c*c == c2:
                    count += 1
        return count * 2

sol = Solution()
print(f'{sol.countTriples(5)} expect 2')
print(f'{sol.countTriples(10)} expect 4')