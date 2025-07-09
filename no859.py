class Solution:
    def makeDict(self, s: str) -> dict:
        s_dict: dict = {}
        for idx, c in enumerate(s):
            if not c in s_dict:
                s_dict[c] = [idx]
            else:
                s_dict[c].append(idx)
        return s_dict


    def buddyStrings(self, s: str, goal: str) -> bool:
        s_dict = self.makeDict(s)
        g_dict = self.makeDict(goal)

        print(s_dict, g_dict)
            
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