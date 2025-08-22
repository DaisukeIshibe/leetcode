class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeros = len(s) - ones
        # 1つだけ1がある場合
        if ones == 1:
            return '0' * zeros + '1'
        # 1が複数ある場合
        return '1' * (ones - 1) + '0' * zeros + '1'

sol = Solution()
print(f'{sol.maximumOddBinaryNumber("010")} expect 001')
print(f'{sol.maximumOddBinaryNumber("0101")} expect 1001')