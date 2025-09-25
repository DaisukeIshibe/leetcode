class Solution:
    def countSeniors(self, details: list[str]) -> int:
        return sum(1 for d in details if int(d[11:13]) >= 60)

sol = Solution()
print(f'{sol.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"])} expect 2')
print(f'{sol.countSeniors(["1313579440F2036","2921522980M5644"])} expect 0')