class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        len_list = []
        for s in strs:
            is_num = True
            for s_ in s:
                try:
                    n = int(s_)
                except:
                    is_num = False
                    break
            
            if is_num:
                len_list.append(int(s))
            else:
                len_list.append(len(s))
        
        return max(len_list)

sol = Solution()
print(f'{sol.maximumValue(["alic3","bob","3","4","00000"])} expect 5')
print(f'{sol.maximumValue(["1","01","001","0001"])} expect 1')