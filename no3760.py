class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))

sol = Solution()
print(f'{sol.maxDistinct("abab")} expect 2')
print(f'{sol.maxDistinct("abcd")} expect 4')
print(f'{sol.maxDistinct("aaaa")} expect 1')