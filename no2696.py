class Solution:
    def minLength(self, s: str) -> int:
        while True:
            if 'AB' in s:
                s = s.replace('AB', '', 1)
            if 'CD' in s:
                s = s.replace('CD', '', 1)
            if ('AB' in s) or ('CD' in s):
                pass
            else:
                break
        return len(s)

sol = Solution()
print(f'{sol.minLength("ABFCACDB")} expect 2')
print(f'{sol.minLength("ACBBD")} expect 5')