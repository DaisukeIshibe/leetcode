class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        # 文字列変換を避け、ビット演算で直接計算
        result = []
        current = 0
        
        for bit in nums:
            # 左シフト + 新しいビット追加 = 次の2進数値
            current = (current << 1 | bit) % 5
            result.append(current == 0)
        
        return result

# さらに最適化版（内包表記）
class SolutionComprehension:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        current = 0
        result = []
        for bit in nums:
            current = (current << 1 | bit) % 5
            result.append(current == 0)
        return result

# ジェネレータ版（メモリ効率最適）
class SolutionGenerator:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        def generate():
            current = 0
            for bit in nums:
                current = (current << 1 | bit) % 5
                yield current == 0
        return list(generate())

# 最速版（pre-allocation）
class SolutionPreAllocated:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        n = len(nums)
        result = [False] * n  # 事前にメモリ確保
        current = 0
        
        for i, bit in enumerate(nums):
            current = (current << 1 | bit) % 5
            result[i] = (current == 0)
        
        return result

sol = Solution()
print(f'{sol.prefixesDivBy5([0,1,1])} expect [true,false,false]')
print(f'{sol.prefixesDivBy5([1,1,1])} expect [false,false,false]')