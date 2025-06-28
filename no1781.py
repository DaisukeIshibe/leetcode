class Solution:
    def caclScore(self, s) -> int:
        c_dict = {}
        for c in s:
            if not c in c_dict:
                c_dict[c] = 1
            else:
                c_dict[c] += 1
        
        v_list = c_dict.values()
        return max(v_list) - min(v_list)
    
    def beautySum(self, s: str) -> int:
        len_s = len(s)
        if len_s <= 2:
            return 0

        total_score = 0
        for i in range(3, len_s + 1):
            for idx in range(0, len_s - i + 1):
                sub_str = s[idx:idx + i]
                #print(sub_str, self.caclScore(sub_str))
                total_score += self.caclScore(sub_str)
        return total_score

sol = Solution()
print(f'{sol.beautySum("aabcb")} expect 5')
print(f'{sol.beautySum("aabcbaa")} expect 17')