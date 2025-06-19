class Solution:
    vowels_dict = {
        'a':True,
        'e':True,
        'i':True,
        'o':True,
        'u':True,
        'A':True,
        'E':True,
        'I':True,
        'O':True,
        'U':True
    }

    def countVowels(self, s: str) -> dict:
        out_dict = {}
        for c in s:
            v:int = 0
            if self.vowels_dict.get(c, False):
                v = 1
            
            if not v in out_dict:
                out_dict[v] = 1
            else:
                out_dict[v] += 1
        return out_dict
    
    def halvesAreAlike(self, s: str) -> bool:
        half_len = len(s) // 2
        first_dict = self.countVowels(s[:half_len])
        last_dict = self.countVowels(s[half_len:])
        return True if first_dict == last_dict else False