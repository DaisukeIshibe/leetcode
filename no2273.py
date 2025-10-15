class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        result = []
        for w in words:
            if not result or sorted(w) != sorted(result[-1]):
                result.append(w)
        return result


sol = Solution()
print(f'{sol.removeAnagrams(["abba","baba","bbaa","cd","cd"])} expect ["abba","cd"]')
print(f'{sol.removeAnagrams(["a","b","c","d","e"])} expect ["a","b","c","d","e"]')
print(f'{sol.removeAnagrams(["a","b","a"])} expect ["a","b","a"]')