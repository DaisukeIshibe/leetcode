class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        w_dict: dict = {}
        for w in words:
            if not w in w_dict:
                w_dict[w] = 1
            else:
                w_dict[w] += 1

        count_rev: int = 0
        for w in words:
            if len(set(w)) == 1:
                continue
            rev_w = w[::-1]
            if rev_w in w_dict:
                add_val = min(w_dict[w], w_dict[rev_w]) * 4
                count_rev += add_val
                if rev_w in w_dict:
                    del w_dict[rev_w]
                if w in w_dict:
                    del w_dict[w]
            else:
                if w in w_dict:
                    del w_dict[w]
        
        if len(w_dict) == 0:
            return count_rev

        count_same: int = 0
        max_key, max_val = sorted(w_dict.items(), key=lambda x:x[1])[-1]
        if max_val == 1:
            return count_rev + 2
        else:
            # consider 
            print(f'left words {w_dict}')
            pass
        
        return count_rev + count_same

sol = Solution()

w = ["lc","cl","gg"]
print(f'words = {w} act = {sol.longestPalindrome(w)} expect = 6')
w = ["ab","ty","yt","lc","cl","ab"]
print(f'words = {w} act = {sol.longestPalindrome(w)} expect = 8')
w = ["cc","ll","xx"]
print(f'words = {w} act = {sol.longestPalindrome(w)} expect = 2')
w = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
print(f'words = {w} act = {sol.longestPalindrome(w)} expect = 22')
w = ["nn","nn","hg","gn","nn","hh","gh","nn","nh","nh"]
print(f'words = {w} act = {sol.longestPalindrome(w)} expect = 14')
w = ["em","pe","mp","ee","pp","me","ep","em","em","me"]
print(f'words = {w} act = {sol.longestPalindrome(w)} expect = 14')