class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        import math
        total = 0
        def sum_if_four(n: int) -> int:
            # early exit: smallest n with 4 divisors is 6 (2*3)
            if n < 6:
                return 0
            s = 1 + n  # include 1 and n
            cnt = 2   # count of divisors so far
            r = math.isqrt(n)
            for i in range(2, r + 1):
                if n % i == 0:
                    j = n // i
                    if i == j:
                        cnt += 1
                        s += i
                    else:
                        cnt += 2
                        s += i + j
                    if cnt > 4:
                        return 0
            return s if cnt == 4 else 0

        for n in nums:
            total += sum_if_four(n)
        return total


if __name__ == '__main__':
    sol = Solution()
    print(f'{sol.sumFourDivisors([21,4,7])} expect 32')
    print(f'{sol.sumFourDivisors([21,21])} expect 64')
    print(f'{sol.sumFourDivisors([1,2,3,4,5])} expect 0')