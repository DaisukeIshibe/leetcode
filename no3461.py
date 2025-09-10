class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(c) for c in s]
        while len(s) > 2:
            s = [(s[i] + s[i + 1]) % 10 for i in range(len(s) - 1)]
        return s[0] == s[1]

sol = Solution()
print(f'{sol.hasSameDigits("3902")} expect True')
print(f'{sol.hasSameDigits("34789")} expect False')