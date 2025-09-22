class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        b_set = set(brokenLetters)
        t_list = text.split()
        count = 0
        for t in t_list:
            for c in t:
                if c in b_set:
                    count += 1
                    break
        return len(t_list) - count

sol = Solution()
print(f'{sol.canBeTypedWords("hello world", "ad")} expect 1')
print(f'{sol.canBeTypedWords("leet code", "lt")} expect 1')
print(f'{sol.canBeTypedWords("leet code", "e")} expect 0')