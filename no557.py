class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w[::-1] for w in s.split()])

sol = Solution()
print(f'{sol.reverseWords("Let's take LeetCode contest")} expect \"s\'teL ekat edoCteeL tsetnoc\"')
print(f'{sol.reverseWords("Mr Ding")} expect "rM gniD"')