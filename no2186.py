class Solution:
    def makeDict(self, s:str) -> dict:
        s_dict:dict = {}
        for i in range(len(s)):
            c = s[i]
            if not c in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1
        
        return s_dict

    def minSteps(self, s: str, t: str) -> int:
        s_dict = self.makeDict(s)
        t_dict = self.makeDict(t)
        common_c:int = 0

        for k, v in s_dict.items():
            if k in t_dict:
                common_c += min(v, t_dict[k])
                
        ans = (len(s) - common_c) + (len(t) - common_c)
        print(f'common_c: {common_c}, len(s): {len(s)}, len(t): {len(t)}')
        return ans

sol = Solution()
print(f'{sol.minSteps("leetcode", "coats")} expect 7') # Expect
print(f'{sol.minSteps("night", "thing")} expect 0') # Expect 0
print(f'{sol.minSteps("cotxazilut", "nahrrmcchxwrieqqdwdpneitkxgnt")} expect 27') # Expect 27