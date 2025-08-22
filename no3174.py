class Solution:
    def clearDigits(self, s: str) -> str:
        import re
        # 数字の直前の文字と数字を削除するパターン
        pattern = r'.\d'
        # 何度も繰り返し削除
        while re.search(pattern, s):
            s = re.sub(pattern, '', s, count=1)
        return s

sol = Solution()
print(f'{sol.clearDigits("abc")} expect abc')
print(f'{sol.clearDigits("cb34")} expect ')