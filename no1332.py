class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # If empty string -> 0 steps
        if not s:
            return 0
        # If s is palindrome -> 1 step
        if s == s[::-1]:
            return 1
        # Otherwise, since only 'a' and 'b' appear, we can remove all 'a's then all 'b's -> 2 steps
        return 2

sol = Solution()
print(f'{sol.removePalindromeSub("ababa")} expect 1')
print(f'{sol.removePalindromeSub("abb")} expect 2')
print(f'{sol.removePalindromeSub("baabb")} expect 2')
print(f'{sol.removePalindromeSub("ababb")} expect 2')