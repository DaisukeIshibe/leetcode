class Solution:
    def pivotInteger(self, n: int) -> int:
        # 数学的解法：x = sqrt(n * (n + 1) / 2)
        total = n * (n + 1) // 2
        x = int(total ** 0.5)
        
        # x が整数かつ条件を満たすかチェック
        if x * x == total:
            return x
        return -1

sol = Solution()
print(f'{sol.pivotInteger(8)} expect 6')
print(f'{sol.pivotInteger(1)} expect 1')
print(f'{sol.pivotInteger(4)} expect -1')