# You are given a 0-indexed string array words.
#
# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
#
# isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.
# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.
#
# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.
class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        count = 0
        n = len(words)
        
        for i in range(n):
            w1 = words[i]
            
            for j in range(i + 1, n):
                w2 = words[j]
                
                # startswith/endswith はC実装で高速
                if w2.startswith(w1) and w2.endswith(w1):
                    count += 1
        
        return count
    
    def countPrefixSuffixPairs_(self, words: list[str]) -> int:
        count:int = 0
        for idx, w in enumerate(words):
            for w_ in words[idx+1:]:
                if w_.startswith(w):
                    if w_.endswith(w):
                        count += 1
        return count

sol = Solution()
print(f'{sol.countPrefixSuffixPairs(["a","aba","ababa","aa"])} expect 4')
print(f'{sol.countPrefixSuffixPairs(["pa","papa","ma","mama"])} expect 2')
print(f'{sol.countPrefixSuffixPairs(["abab","ab"])} expect 0')
print(f'{sol.countPrefixSuffixPairs(["a","abb"])} expect 0')