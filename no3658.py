class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_total:int = n * n
        even_total:int = (1 + n) * n
        
        import math
        return math.gcd(odd_total, even_total)

sol = Solution()
print(f'{sol.gcdOfOddEvenSums(4)} expect 4')
print(f'{sol.gcdOfOddEvenSums(5)} expect 5')