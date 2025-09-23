class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        if not brokenLetters:
            return len(text.split())
        
        b_set = set(brokenLetters)
        return sum(1 for word in text.split() if not any(c in b_set for c in word))

sol = Solution()
print(f'{sol.canBeTypedWords("hello world", "ad")} expect 1')
print(f'{sol.canBeTypedWords("leet code", "lt")} expect 1')
print(f'{sol.canBeTypedWords("leet code", "e")} expect 0')