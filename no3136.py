class Solution:
    vow_dict = {
        'a':True, 'i':True, 'u':True, 'e':True, 'o':True,
        'A':True, 'I':True, 'U':True, 'E':True, 'O':True
	}
    
    num_dict = {
        '0':True, '1':True, '2':True, '3':True, '4':True,
        '5':True, '6':True, '7':True, '8':True, '9':True
	}
    
    ng_dict = {
        '@':True, '$':True, '#':True, '(':True, ')':True,
        '=':True, '!':True, '"':True, '&':True, '/':True,
	}
    
    def isValid(self, word: str) -> bool:
        len_w = len(word)
        if len_w < 3:
            return False

        vow_count: int = 0
        con_count: int = 0
        for i in range(len_w):
            c = word[i]
            if c in self.ng_dict:
                return False
            else:
                if c in self.vow_dict:
                    vow_count += 1
                else:
                    if c in self.num_dict:
                        pass
                    else:
                        con_count += 1
        if vow_count > 0 and con_count > 0:
            return True
        else:
            return False


sol = Solution()
print(f'{sol.isValid("234Adas")} expect True')
print(f'{sol.isValid("b3")} expect False')
print(f'{sol.isValid("a3$e")} expect False')
print(f'{sol.isValid("3pp")} expect False')
