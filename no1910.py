class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            if part in s:
                s = s.replace(part, '', 1)
            else:
                break
        return s

sol = Solution()
print(f'{sol.removeOccurrences("daabcbaabcbc", "abc")} expect dab')
print(f'{sol.removeOccurrences("axxxxyyyyb", "xy")} expect ab')
print(f'{sol.removeOccurrences("aabababa", "aba")} expect ba')