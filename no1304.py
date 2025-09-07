class Solution:
    def sumZero(self, n: int) -> list[int]:
        half_n = n // 2
        out_list = [i + 1 for i in range(half_n)] + [-(i + 1) for i in range(half_n)]
        if n % 2:
            out_list.append(0)
        return out_list

sol = Solution()
ans_no1 = sum(sol.sumZero(5))
ans_no2 = sum(sol.sumZero(3))
ans_no3 = sum(sol.sumZero(1))

if (ans_no1 + ans_no2 + ans_no3) == 0:
    print('OK')
else:
    print('NG')