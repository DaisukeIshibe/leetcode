class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        import collections
        s_count = collections.Counter(s)
        if len(s_count) == sum(s_count.values()):
            return 0
        count_double:int = 0
        count_trible:int = 0
        for k, v in s_count.items():
            if v == 2:
                count_double += 1
            if v >= 3:
                count_trible += 1
        total: int = count_double * (len(s_count) - 1)
        print(s_count, count_double, count_trible)
        return 0

sol = Solution()
print(f'{sol.countPalindromicSubsequence("aabca")} expect 3')
print(f'{sol.countPalindromicSubsequence("adc")} expect 0')
print(f'{sol.countPalindromicSubsequence("bbcbaba")} expect 4')