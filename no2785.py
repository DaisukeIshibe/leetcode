class Solution:
    vowels_dict = {'a','i','u','e','o','A','I','U','E','O'}

    def sortVowels(self, s: str) -> str:
        out_list = []
        vowels_list = []
        for c in s:
            if c in self.vowels_dict:
                out_list.append('-')
                vowels_list.append(c)
            else:
                out_list.append(c)
        vowels_list = sorted(vowels_list)
        for idx, c in enumerate(out_list):
            if c == '-':
                out_list[idx] = vowels_list.pop(0)
        #print(vowels_list)
        return ''.join(out_list)


sol = Solution()
print(f'{sol.sortVowels("lEetcOde")} expect "lEOtcede"')
print(f'{sol.sortVowels("lYmpH")} expect "lYmpH"')