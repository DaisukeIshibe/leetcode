class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        効率的な解法：桁の出現回数を比較
        時間計算量: O(log^2 n)
        空間計算量: O(1)
        """
        def count_digits(num):
            """数字の各桁の出現回数をカウント"""
            count = [0] * 10
            for digit in str(num):
                count[int(digit)] += 1
            return count
        
        # nの桁数を取得
        n_digits = len(str(n))
        n_count = count_digits(n)
        
        # nの桁数に対応する2の累乗の範囲を計算
        # 最小: 10^(digits-1), 最大: 10^digits - 1
        min_power = 10 ** (n_digits - 1) if n_digits > 1 else 1
        max_power = 10 ** n_digits - 1
        
        # 2の累乗を順番に生成して比較
        power_of_2 = 1
        while power_of_2 <= max_power:
            if power_of_2 >= min_power:
                if count_digits(power_of_2) == n_count:
                    return True
            power_of_2 *= 2
        
        return False
    
    def reorderedPowerOf2_alternative(self, n: int) -> bool:
        """
        代替解法：すべての順列を生成して2の累乗をチェック
        時間計算量: O(n! * log n) - 効率が悪い
        """
        import itertools
        
        def is_power_of_2(num):
            return num > 0 and (num & (num - 1)) == 0
        
        n_str = str(n)
        
        # すべての順列を生成
        for perm in itertools.permutations(n_str):
            # 先頭が0でない場合のみ処理
            if perm[0] != '0':
                num = int(''.join(perm))
                if is_power_of_2(num):
                    return True
        
        return False

# テスト関数
def test_solution():
    sol = Solution()
    
    test_cases = [
        (1, True),      # 1 は 2^0
        (10, False),    # 10 の桁を並び替えても2の累乗にならない (01は先頭0なのでNG)
        (16, True),     # 16 は 2^4
        (24, False),    # 24 → digits [2,4] → 可能な数: 24, 42 (どちらも2の累乗ではない)
        (125, True),    # 125 → digits [1,2,5] → 可能な数に 512 = 2^9 が含まれる
        (46, True),     # 46 → digits [4,6] → 64 = 2^6
        (1024, True),   # 1024 自体が 2^10
        (32, True),     # 32 は 2^5
        (321, False),   # 321 → digits [3,2,1] → すべて2の累乗ではない
    ]
    
    print("=== テスト結果 ===")
    for n, expected in test_cases:
        result1 = sol.reorderedPowerOf2(n)
        result2 = sol.reorderedPowerOf2_alternative(n)
        
        status1 = "✓" if result1 == expected else "✗"
        status2 = "✓" if result2 == expected else "✗"
        
        print(f"n={n:4d}: 効率版={result1} {status1}, 順列版={result2} {status2}, 期待値={expected}")
        
        # 詳細な分析（125の場合）
        if n == 125:
            print(f"  → digits [1,2,5] から作れる数:")
            digits = "125"
            import itertools
            numbers = []
            for perm in itertools.permutations(digits):
                if perm[0] != '0':
                    num = int(''.join(perm))
                    numbers.append(num)
            
            powers_of_2 = [2**i for i in range(20)]
            valid_powers = [num for num in numbers if num in powers_of_2]
            print(f"     可能な数: {sorted(set(numbers))}")
            print(f"     2の累乗: {valid_powers}")

# パフォーマンステスト
def performance_test():
    import time
    sol = Solution()
    
    test_numbers = [123456789, 987654321, 1023, 2048]
    
    print("\n=== パフォーマンステスト ===")
    for n in test_numbers:
        start = time.time()
        result1 = sol.reorderedPowerOf2(n)
        time1 = time.time() - start
        
        start = time.time()
        result2 = sol.reorderedPowerOf2_alternative(n)
        time2 = time.time() - start
        
        print(f"n={n}: 効率版={result1} ({time1:.4f}s), 順列版={result2} ({time2:.4f}s)")

if __name__ == "__main__":
    test_solution()
    performance_test()
