class Solution:
    def make_dict(self, w:str) -> dict:
        w_dict:dict = {}
        for i in range(len(w)):
            c = w[i]
            if not c in w_dict:
                w_dict[c] = 1
            else:
                w_dict[c] += 1

        return w_dict

    def countCharacters(self, words: list[str], chars: str) -> int:
        dict_list:list = []
        for w in words:
            dict_list.append(self.make_dict(w))
        
        c_dict = self.make_dict(chars)

        match_count:int = 0
        for d in dict_list:
            match_flag:bool = True
            for k, v in d.items():
                if k in c_dict:
                    if v <= c_dict[k]:
                        pass
                    else:
                        match_flag = False
                        break
                else:
                    match_flag = False
                    break
                
            if match_flag:
                match_count += sum(d.values())
        return match_count

# Test case
s = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
print(f'words = {words} chars = {chars} act = {s.countCharacters(words, chars)} expect = 6')
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(f'words = {words} chars = {chars} act = {s.countCharacters(words, chars)} expect = 10')