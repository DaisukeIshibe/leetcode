class Solution:
    def minimumLength(self, s: str) -> int:
        len_s = len(s)
        if len_s <= 2:
            return len_s
        
        s_list = list(s)
        s_dict: dict = {}
        for idx, c in enumerate(s_list):
            if not c in s_dict:
                s_dict[c] = [idx]
            else:
                s_dict[c].append(idx)
                if len(s_dict[c]) >= 3:
                    min_n = min(s_dict[c])
                    max_n = min(s_dict[c])
        return 0

sol = Solution()
print(f'{sol.minimumLength("abaacbcbb")} Expect 5')
print(f'{sol.minimumLength("aa")} Expect 2')