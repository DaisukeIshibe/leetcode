class Solution:
    def makeDict(self, word: str) -> dict:
        w_dict: dict = {}
        for c in word:
            if not c in w_dict:
                w_dict[c] = 1
            else:
                w_dict[c] += 1
        return w_dict

    def commonChars(self, words: list[str]) -> list[str]:
        dict_list = [self.makeDict(w) for w in words]
        key_list = []
        for d in dict_list:
            key_list.extend(list(d.keys()))
        k_dict = self.makeDict(key_list)
        len_w = len(words)
        common_list = [k for k, v in k_dict.items() if v == len_w]
        out_list = []
        for c in common_list:
            rep_list = []
            for d in dict_list:
                rep_list.append(d[c])
            out_list.extend([c] * min(rep_list))
                
        #print(dict_list, '\n', common_list, '\n', out_list)
        return out_list

sol = Solution()
words = ["bella","label","roller"]
print(f'{sol.commonChars(words)} expect ["e","l","l"]')

words = ["cool","lock","cook"]
print(f'{sol.commonChars(words)} expect ["c","o"]')