class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(100 * s.count(letter)/len(s))

sol = Solution()
print(f'{sol.percentageLetter("foobar", "o")} expect 33')
print(f'{sol.percentageLetter("jjjj", "k")} expect 0')