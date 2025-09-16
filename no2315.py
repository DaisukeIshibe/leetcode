class Solution:
    def countAsterisks(self, s: str) -> int:
        asta_count = 0
        for idx, e in enumerate(s.split('|')):
            if idx % 2 == 0:
                asta_count += e.count('*')
        return asta_count

sol = Solution()
print(f'{sol.countAsterisks("l|*e*et|c**o|*de|")} expect 2')
print(f'{sol.countAsterisks("iamprogrammer")} expect 0')
print(f'{sol.countAsterisks("yo|uar|e**|b|e***au|tifu|l")} expect 5')