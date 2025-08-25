class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good_count: int = 0
        for i in range(len(s) - 2):
            sub_str = s[i:i + 3]
            if len(set(sub_str)) == 3:
                good_count += 1
        return good_count

sol = Solution()
print(f'{sol.countGoodSubstrings("xyzzaz")} expect 1')
print(f'{sol.countGoodSubstrings("aababcabc")} expect 4')