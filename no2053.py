class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        import collections
        count_iter = collections.Counter(arr)
        count = 0
        for c in count_iter:
            c_ = count_iter[c]
            if c_ == 1:
                count += c_
                if count == k:
                    return c
        return ''

sol = Solution()
print(f'{sol.kthDistinct(["d","b","c","b","c","a"], 2)} expect a')
print(f'{sol.kthDistinct(["aaa","aa","a"], 1)} expect aaa')
print(f'{sol.kthDistinct(["a","b","a"], 3)} expect')