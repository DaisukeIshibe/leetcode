class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return 'a' * (n - 1) + 'b'
        else:
            return 'a' * n

sol = Solution()
print(f'{sol.generateTheString(4)} expect "pppz"')
print(f'{sol.generateTheString(2)} expect "xy"')
print(f'{sol.generateTheString(7)} expect "holasss"')