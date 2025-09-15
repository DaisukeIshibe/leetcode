class Solution:
    def stringHash(self, s: str, k: int) -> str:
        len_s = len(s)
        idx = 0
        out_str:str = ''
        while idx < len_s:
            sub_str = s[idx:idx + k]
            sub_total = 0
            for i in range(k):
                c = sub_str[i]
                sub_total += (ord(c) - 97)
            s_ = chr((sub_total % 26) + 97)
            idx += k
            out_str += s_
            #print(s, sub_str, s_)
        return out_str

sol = Solution()
print(f'{sol.stringHash("abcd", 2)} expect bf')
print(f'{sol.stringHash("mxz", 3)} expect i')
print(f'{sol.stringHash("a", 1)} expect a')
print(f'{sol.stringHash("ahauqh", 2)} expect hux')