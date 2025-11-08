class Solution:
    def sortString(self, s: str) -> str:
        import collections
        s_count = collections.Counter(s)
        s_list = sorted(set(s))
        s_rev_list = sorted(s_list, reverse=True)
        out_str: str = ''
        #print(s_count, s_list, s_rev_list)
        while True:
            for s_ in s_list:
                if s_count[s_] > 0:
                    out_str += s_
                    s_count[s_] -= 1
            for s_ in s_rev_list:
                if s_count[s_] > 0:
                    out_str += s_
                    s_count[s_] -= 1
                    
            break_flag = True
            for _, val in s_count.items():
                if val != 0:
                    break_flag = False

            if break_flag:
                break

        return out_str

sol = Solution()
print(f'{sol.sortString("aaaabbbbcccc")} expect "abccbaabccba"')
print(f'{sol.sortString("rat")} expect "art"')