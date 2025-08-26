class Solution:
    def countBits(self, n: int) -> list[int]:
        return [bin(i).count('1') for i in range(n + 1)]
