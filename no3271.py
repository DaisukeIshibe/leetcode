class Solution:
    def stringHash(self, s: str, k: int) -> str:
        for c in s:
            a_c = ord(c) - 97
            print(f'{c} {a_c}')
        return ''

sol = Solution()
print(f'{sol.stringHash("abcd", 2)} expect bf')
print(f'{sol.stringHash("mxz", 3)} expect i')