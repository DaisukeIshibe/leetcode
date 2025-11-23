class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        count: int = 0
        for w in words:
            if s.startswith(w):
                count += 1
        return count

sol = Solution()
print(f'{sol.countPrefixes(["a","b","c","ab","bc","abc"], "abc")} expect 3')
print(f'{sol.countPrefixes(["a","a"], "aa")} expect 2')