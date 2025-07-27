class Solution:
    def makeDict(self, s: str) -> dict:
        s_dict: dict = {}
        for c in s:
            if not c in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1
        return s_dict

    def minSteps(self, s: str, t: str) -> int:
        s_dict = self.makeDict(s)
        t_dict = self.makeDict(t)
        match_count: int = 0
        for key_s in s_dict.keys():
            if key_s in t_dict:
                diff = min(s_dict[key_s], t_dict[key_s])
                match_count += diff
        return len(s) - match_count

def check(a, b):
    if a == b:
        print('OK')
    else:
        print(f'{a} is not {b}')

sol = Solution()
s = "bab"
t = "aba"
check(sol.minSteps(s, t), 1)

s = "leetcode"
t = "practice"
check(sol.minSteps(s, t), 5)

s = "anagram"
t = "mangaar"
check(sol.minSteps(s, t), 0)
