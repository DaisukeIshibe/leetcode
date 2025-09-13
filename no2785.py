class Solution:
    vowels_set = set('aiueoAIUEO')

    def sortVowels(self, s: str) -> str:
        out_list = list(s)
        vowels = [c for c in out_list if c in self.vowels_set]
        vowels.sort()
        v_idx = 0
        for i, c in enumerate(out_list):
            if c in self.vowels_set:
                out_list[i] = vowels[v_idx]
                v_idx += 1
        return ''.join(out_list)


sol = Solution()
print(f'{sol.sortVowels("lEetcOde")} expect "lEOtcede"')
print(f'{sol.sortVowels("lYmpH")} expect "lYmpH"')