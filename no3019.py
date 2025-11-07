class Solution:
    def countKeyChanges(self, s: str) -> int:
        s_low = s.lower()
        ch_list = []
        for i in range(len(s_low)):
            c = s_low[i]
            if i == 0:
                ch_list.append(c)
            else:
                if ch_list[-1] != c:
                    ch_list.append(c)
        #print(ch_list)
        return len(ch_list) - 1
    
sol = Solution()
print(f'{sol.countKeyChanges("aAbBcC")} expect 2')
print(f'{sol.countKeyChanges("AaAaAaaA")} expect 0')
print(f'{sol.countKeyChanges("mDVD")} expect 3')