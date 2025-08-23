class Solution:
    def lengthOfLongestSubstring_(self, s: str) -> int:
        max_len = len(set(s))
        len_s = len(s)
        
        while True:
            if max_len == 1:
                break
            for i in range(len_s - max_len + 1):
                str_ = s[i:max_len + i]
                if len(set(str_)) == len(str_):
                    return max_len
            max_len -= 1
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        # スライディングウィンドウ法で高速化
        char_set = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
    
sol = Solution()
print(f'{sol.lengthOfLongestSubstring("abcabcbb")} expect 3')
print(f'{sol.lengthOfLongestSubstring("bbbbb")} expect 1')
print(f'{sol.lengthOfLongestSubstring("pwwkew")} expect 3')
print(f'{sol.lengthOfLongestSubstring("")} expect 0')
print(f'{sol.lengthOfLongestSubstring(" ")} expect 1')
print(f'{sol.lengthOfLongestSubstring("aa")} expect 1')
print(f'{sol.lengthOfLongestSubstring("au")} expect 2')
print(f'{sol.lengthOfLongestSubstring("dvdf")} expect 3')