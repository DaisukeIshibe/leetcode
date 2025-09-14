class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        t = n // 2
        div_list = []
        for i in range(1, t + 1):
            if n % i == 0:
                div_list.append(i)
        div_list.append(n)
        if len(div_list) >= k:
            return div_list[k - 1]
        else:
            return -1

sol = Solution()
print(f'{sol.kthFactor(12, 3)} expect 3')
print(f'{sol.kthFactor(7, 2)} expect 7')
print(f'{sol.kthFactor(4, 4)} expect -1')