class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_dict = {'a':0, 'i':0, 'u':0, 'e':0, 'o':0}
        for c in s:
            pass
        return 0

sol = Solution()
print(f'{sol.findTheLongestSubstring("eleetminicoworoep")} expect 13')
print(f'{sol.findTheLongestSubstring("leetcodeisgreat")} expect 5')
print(f'{sol.findTheLongestSubstring("bcbcbc")} expect 6')