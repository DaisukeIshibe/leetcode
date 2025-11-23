class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        # frozensetを使用（setより高速な検索）
        vowels = frozenset('aeiou')
        
        # 内包表記とsum()で処理を高速化
        return sum(1 for word in words[left:right+1] 
                  if word and word[0] in vowels and word[-1] in vowels)

# さらなる最適化版（ビット演算使用）
class SolutionBitwise:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        # ASCII値を使ったビット演算（最高速）
        vowel_bits = (1 << ord('a')) | (1 << ord('e')) | (1 << ord('i')) | (1 << ord('o')) | (1 << ord('u'))
        
        count = 0
        for i in range(left, right + 1):
            word = words[i]
            if word and (vowel_bits >> ord(word[0])) & 1 and (vowel_bits >> ord(word[-1])) & 1:
                count += 1
        return count

# インデックス最適化版
class SolutionIndexOptimized:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = frozenset('aeiou')
        count = 0
        
        # スライシングを避けて直接インデックスアクセス
        for i in range(left, right + 1):
            word = words[i]
            if word and word[0] in vowels and word[-1] in vowels:
                count += 1
        return count

# 関数型プログラミング版（最も簡潔）
class SolutionFunctional:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = set('aeiou')
        return sum(word[0] in vowels and word[-1] in vowels 
                  for word in words[left:right+1] if word)

# プリコンパイル版（大量データ向け）
class SolutionPrecompiled:
    _vowels = frozenset('aeiou')
    _is_vowel = _vowels.__contains__  # メソッド参照をキャッシュ
    
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        is_vowel = self._is_vowel
        return sum(1 for word in words[left:right+1] 
                  if word and is_vowel(word[0]) and is_vowel(word[-1]))

# テスト実行
sol = Solution()
sol_bitwise = SolutionBitwise()
sol_optimized = SolutionIndexOptimized()
sol_functional = SolutionFunctional()
sol_precompiled = SolutionPrecompiled()

test_cases = [
    (["are","amy","u"], 0, 2, 2),
    (["hey","aeo","mu","ooo","artro"], 1, 4, 3),
    (["a", "e", "i", "o", "u"], 0, 4, 5),
    (["hello", "world"], 0, 1, 0)
]

for words, left, right, expected in test_cases:
    basic = sol.vowelStrings(words, left, right)
    bitwise = sol_bitwise.vowelStrings(words, left, right)
    optimized = sol_optimized.vowelStrings(words, left, right)
    functional = sol_functional.vowelStrings(words, left, right)
    precompiled = sol_precompiled.vowelStrings(words, left, right)
    
    print(f'Input: {words}, {left}, {right}')
    print(f'Basic: {basic}, Bitwise: {bitwise}, Optimized: {optimized}')
    print(f'Functional: {functional}, Precompiled: {precompiled}, Expected: {expected}')
    print('---')