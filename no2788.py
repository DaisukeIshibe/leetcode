class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        # リスト内包表記で高速化
        return [s for w in words for s in w.split(separator) if s]

sol = Solution()
print(f'{sol.splitWordsBySeparator(["one.two.three","four.five","six"], ".")} expect ["one","two","three","four","five","six"]')
print(f'{sol.splitWordsBySeparator(["$easy$","$problem$"], "$")} expect ["easy","problem"]')
print(f'{sol.splitWordsBySeparator(["|||"], "|")} expect ')
