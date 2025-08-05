class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 特殊ケース
        if n == 0:
            return 1.0
        
        # 負数の指数の場合、x^(-n) = 1 / x^n
        if n < 0:
            x = 1 / x
            n = -n
        
        # 分割統治法による高速べき乗計算 O(log n)
        result = 1.0
        current_power = x
        
        while n > 0:
            # nが奇数の場合、現在の累乗を結果に掛ける
            if n % 2 == 1:
                result *= current_power
            
            # 累乗を2倍にし、指数を半分にする
            current_power *= current_power
            n //= 2
        
        return result

sol = Solution()
print(f'{sol.myPow(2, 10)} expect 1024')
print(f'{sol.myPow(2.1, 3)} expect 9.261')
print(f'{sol.myPow(2, -2)} expect 0.25')
print(f'{sol.myPow(0.00001, 2147483647)} expect 0.0')