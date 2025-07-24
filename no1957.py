class Solution:
    def makeFancyString(self, s: str) -> str:
        s_str: str = ''
        len_s = len(s)
        for i in range(len_s - 1):
            c_curr = s[i]
            c_next = s[i + 1]
            s_str += c_curr
            if c_curr != c_next:
                s_str += ' '
            
            if i == (len_s - 2):
                s_str += c_next

        out_list = []
        for s_ in s_str.split():
            if len(s_) <= 2:
                out_list.append(s_)
            else:
                out_list.append(s_[:2])
        return ''.join(out_list)

    
sol = Solution()
print(f'{sol.makeFancyString("leeetcode")} expect "leetcode"')
print(f'{sol.makeFancyString("aaabaaaa")} expect "aabaa"')
print(f'{sol.makeFancyString("aab")} expect "aab"')