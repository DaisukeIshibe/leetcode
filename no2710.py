class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while True:
            if num.endswith('0'):
                num = num[:(len(num)-1)]
            else:
                break
        return num

sol = Solution()

print(f'{sol.removeTrailingZeros("51230100")} expect 512301')
print(f'{sol.removeTrailingZeros("123")} expect 123')