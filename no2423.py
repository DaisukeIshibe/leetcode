class Solution:
    def equalFrequency(self, word: str) -> bool:
        w_dict: dict = {}
        max_word: str = ''
        min_word: str = ''
        for w in word:
            if not w in w_dict:
                w_dict[w] = 1
            else:
                w_dict[w] += 1
        
        sorted_list = sorted(w_dict.items(), key=lambda x:x[1])
        min_word = sorted_list[0][0]
        max_word = sorted_list[-1][0]

        w1_dict = w_dict.copy()
        w1_dict[max_word] -= 1
        if w1_dict[max_word] == 0:
            del w1_dict[max_word]
        if len(list(set(w1_dict.values()))) == 1:
            return True
        
        w_dict[min_word] -= 1
        if w_dict[min_word] == 0:
            del w_dict[min_word]
        if len(list(set(w_dict.values()))) == 1:
            return True
        
        return False

sol = Solution()
print(f'{sol.equalFrequency("abcc")} expect True')
print(f'{sol.equalFrequency("aazz")} expect False')
print(f'{sol.equalFrequency("bac")} expect True')
print(f'{sol.equalFrequency("cccaa")} expect True')
print(f'{sol.equalFrequency("abbcc")} expect True')
print(f'{sol.equalFrequency("cccd")} expect True')
