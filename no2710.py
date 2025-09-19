class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')

sol = Solution()

print(f'{sol.removeTrailingZeros("51230100")} expect 512301')
print(f'{sol.removeTrailingZeros("123")} expect 123')