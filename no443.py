class Solution:
    def compress(self, chars: list[str]) -> int:
        len_chars = len(chars)
        if len_chars == 1:
            return 1

        idx = 0
        out_list = []
        for i in range(len_chars - 1):
            pass
        return 0

sol = Solution()
print(f'{sol.compress(["a","a","b","b","c","c","c"])} expect 6 / "a2b2c3"')
print(f'{sol.compress(["a"])} expect 1 / "a"')
print(f'{sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])} expect 4 / "["a","b","1","2"]"')
print(f'{sol.compress(["a","a","a","b","b","a","a"])}, expect 6 / "["a","3","b","2","a","2"]"')