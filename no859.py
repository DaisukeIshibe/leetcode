class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        len_s = len(s)
        if len_s <= 2:
            return False
    
        s_list = [(c, idx) for idx, c in enumerate(s)]
        g_list = [(g, idx) for idx, g in enumerate(goal)]
        for (c, c_idx), (g, g_idx) in zip(s_list, g_list):
            if c != g:
                pass
        return False
    
sol = Solution()
s = "ab"
goal = "ba"
print(f'{sol.buddyStrings(s, goal)} expect True') # Expect True
s = "ab"
goal = "ab"
print(f'{sol.buddyStrings(s, goal)} expect False') # Expect False
s = "aa"
goal = "aa"
print(f'{sol.buddyStrings(s, goal)} expect True') # Expect True
s = "abcd"
goal = "badc"
print(f'{sol.buddyStrings(s, goal)} expect False') # Expect False
s = "abcaa"
goal = "abcbb"
print(f'{sol.buddyStrings(s, goal)} expect False') # Expect False
s = "ab"
goal = "ca"
print(f'{sol.buddyStrings(s, goal)} expect False') # Expect False
s = "abc"
goal = "acd"
print(f'{sol.buddyStrings(s, goal)} expect False') # Expect False
s = "abab"
goal = "abab"
print(f'{sol.buddyStrings(s, goal)} expect True') # Expect True
s = "abcd"
goal = "abcd"
print(f'{sol.buddyStrings(s, goal)} expect False') # Expect False