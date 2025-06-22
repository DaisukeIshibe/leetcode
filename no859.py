class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) == 1:
             return False
        if len(s) == 2:
            if s[::-1] == goal:
                return True
            else:
                return False
        
        if s == goal:
            return True
             
        w_count = 0
        w_list = []
        for c_s, c_g in zip(s, goal):
            if c_s != c_g:
                w_list.append([c_s, c_g])
                w_count +=1
        
        if w_count == 2:
            if w_list[0] == w_list[1]:
                return False
            else:
                if w_list[0][1] == w_list[1][0] and w_list[0][0] == w_list[1][1]:
                    return True
                else:
                    return False
        else:
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