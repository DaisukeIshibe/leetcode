import math
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n+4, 4)
# 
sol = Solution()
print(f'{sol.countVowelStrings(1)} expect 5')
print(f'{sol.countVowelStrings(2)} expect 15')
print(f'{sol.countVowelStrings(33)} expect 66045')