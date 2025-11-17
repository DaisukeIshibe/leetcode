from collections import Counter, defaultdict

class Solution:
    def similarPairs(self, words: list[str]) -> int:
        # 各単語の文字セットを正規化してグループ化
        signature_count = Counter()
        
        for word in words:
            # 文字セットを文字列として正規化
            signature = ''.join(sorted(set(word)))
            signature_count[signature] += 1
        
        # 各グループ内でのペア数を計算
        total_pairs = 0
        for count in signature_count.values():
            if count > 1:
                # nC2 = n * (n-1) / 2
                total_pairs += count * (count - 1) // 2
        
        return total_pairs

# より高速な版
class SolutionOptimized:
    def similarPairs(self, words: list[str]) -> int:
        # defaultdictで効率化
        groups = defaultdict(int)
        
        for word in words:
            # frozensetを使ってハッシュ可能な署名を作成
            signature = frozenset(word)
            groups[signature] += 1
        
        # ワンライナーで組み合わせ計算
        return sum(count * (count - 1) // 2 for count in groups.values() if count > 1)

# 最高速版（ビット操作使用）
class SolutionFastest:
    def similarPairs(self, words: list[str]) -> int:
        groups = defaultdict(int)
        
        for word in words:
            # ビットマスクで文字セットを表現（小文字のみの場合）
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            groups[mask] += 1
        
        return sum(count * (count - 1) // 2 for count in groups.values() if count > 1)

# デバッグ用の詳細版
class SolutionDebug:
    def similarPairs(self, words: list[str]) -> int:
        print("=== デバッグ情報 ===")
        groups = defaultdict(list)
        
        for word in words:
            signature = ''.join(sorted(set(word)))
            groups[signature].append(word)
            print(f"Word: '{word}' -> Signature: '{signature}'")
        
        print("\n=== グループ化結果 ===")
        total_pairs = 0
        for signature, word_list in groups.items():
            count = len(word_list)
            pairs = count * (count - 1) // 2 if count > 1 else 0
            print(f"Signature '{signature}': {word_list} -> {count} words, {pairs} pairs")
            total_pairs += pairs
        
        print(f"\n=== 総ペア数: {total_pairs} ===")
        return total_pairs

# テスト実行
sol = Solution()
sol_opt = SolutionOptimized()
sol_fast = SolutionFastest()
sol_debug = SolutionDebug()

print("=== 修正版結果 ===")
test_cases = [
    ["aba","aabb","abcd","bac","aabc"],
    ["aabb","ab","ba"],
    ["nba","cba","dba"]
]

expected = [2, 3, 0]

for i, (test_case, expect) in enumerate(zip(test_cases, expected)):
    print(f"\nTest {i+1}: {test_case}")
    result = sol.similarPairs(test_case)
    result_opt = sol_opt.similarPairs(test_case)
    result_fast = sol_fast.similarPairs(test_case)
    
    print(f"  Original:  {result}")
    print(f"  Optimized: {result_opt}")
    print(f"  Fastest:   {result_fast}")
    print(f"  Expected:  {expect}")
    print(f"  Status: {'✓' if result == expect else '✗'}")

print("\n=== デバッグ実行（Test 1） ===")
sol_debug.similarPairs(["aba","aabb","abcd","bac","aabc"])

print("\n=== 大量データテスト ===")
large_test = ["dcedceadceceaeddcedc","dddcebcedcdbaeaaaeab","eecbeddbddeadcbbbdbb",
              "decbcbebbddceacdeadd","ccbddbaedcadedbcaaae","dddcaadaceaedcdceedd",
              "bbeddbcbbccddcaceeea","bdabacbbdadabbbddaea"]
result_large = sol.similarPairs(large_test)
print(f'Large test result: {result_large} (expect 16)')