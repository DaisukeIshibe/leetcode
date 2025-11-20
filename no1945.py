class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ascii_str: str = ''
        for c in s:
            ascii_str += str(ord(c) - 96)

        for _ in range(k):
            total: int = 0
            for c in ascii_str:
                total += int(c)
            ascii_str = str(total)
            
        return total

sol = Solution()
print(f'{sol.getLucky("iiii", 1)} expect 36')
print(f'{sol.getLucky("leetcode", 2)} expect 6')
print(f'{sol.getLucky("zbax", 2)} expect 8')