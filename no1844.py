class Solution:
    def replaceDigits(self, s: str) -> str:
        num_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        out_str:str = ''
        for idx, c in enumerate(s):
            if c in num_set:
                out_str += chr(ord(s[idx - 1]) + int(c))
            else:
                out_str += c
        return out_str

sol = Solution()
print(f'{sol.replaceDigits("a1c1e1")} expect "abcdef"')
print(f'{sol.replaceDigits("a1b2c3d4e")} expect "abbdcfdhe"')