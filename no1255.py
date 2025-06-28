class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        import string
        alphabet_dict = {a:v for a, v in zip(list(string.ascii_lowercase), score)}
        score_list = []
        for w in words:
            score = 0
            for c in w:
                score += alphabet_dict[c]
            score_list.append(score)
        return max(score_list)

sol = Solution()
words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
print(f'{sol.maxScoreWords(words, letters, score)} expect 23')