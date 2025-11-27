class Solution:
    def greatestLetter(self, s: str) -> str:
        abc_low_list = [chr(ord("a") + i) for i in range(26)]
        abc_low_dict = {a:0 for a in abc_low_list}
        abc_hi_list = [a.upper() for a in abc_low_list]
        abc_hi_dict = {a:0 for a in abc_hi_list}
        
        for s_ in set(s):
            if s_ in abc_low_dict:
                abc_low_dict[s_] += 1
            if s_ in abc_hi_dict:
                abc_hi_dict[s_] += 1
        
        out_list = []
        for low, up in zip(abc_low_dict.keys(), abc_hi_dict.keys()):
            low_v = abc_low_dict[low]
            up_v = abc_hi_dict[up]
            if (low_v > 0) and (up_v > 0):
                out_list.append(up)
        
        if out_list == []:
            return ""
        else:
            return sorted(out_list)[-1]

sol = Solution()
print(f'{sol.greatestLetter("lEeTcOdE")} expect E')
print(f'{sol.greatestLetter("arRAzFif")} expect R')
print(f'{sol.greatestLetter("AbCdEfGhIjK")} expect ""')