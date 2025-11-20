class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        # setを使ってO(1)の検索時間を実現
        num_set = set(nums)
        
        # original値を2倍にしながら存在チェック
        while original in num_set:
            original *= 2
        
        return original

# さらなる最適化版（大きな数値に対応）
class SolutionOptimized:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        num_set = set(nums)
        
        # original値が非常に大きくなるのを防ぐため、上限チェックを追加
        while original in num_set and original <= 10**6:  # LeetCodeの制約に応じて調整
            original *= 2
        
        return original

# ビット演算を使った版（さらに高速）
class SolutionBitwise:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        num_set = set(nums)
        
        # ビットシフトで2倍にする（乗算より高速）
        while original in num_set:
            original <<= 1  # original *= 2 と同等だが高速
        
        return original

# 最大値チェック付きの版
class SolutionWithBounds:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        if not nums:
            return original
        
        num_set = set(nums)
        max_val = max(nums)
        
        # 配列の最大値の2倍まででループを止める最適化
        while original in num_set and original <= max_val:
            original <<= 1
        
        return original