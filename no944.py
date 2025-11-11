class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        if not strs:
            return 0
        
        wrong_num = 0
        # 列ごとに直接チェック
        for col in range(len(strs[0])):
            # 前の文字と比較して降順があるかチェック
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row-1][col]:
                    wrong_num += 1
                    break  # この列は削除対象なので次の列へ
        
        return wrong_num

# さらに最適化されたワンライナー版
class SolutionOptimized:
    def minDeletionSize(self, strs: list[str]) -> int:
        return sum(
            any(strs[i][j] < strs[i-1][j] for i in range(1, len(strs)))
            for j in range(len(strs[0]))
        )

# NumPy使用版（大量データに最適）
class SolutionNumPy:
    def minDeletionSize(self, strs: list[str]) -> int:
        import numpy as np
        
        # 文字列を2D配列に変換
        char_matrix = np.array([[ord(c) for c in s] for s in strs])
        
        # 各列で降順があるかチェック
        return np.sum(np.any(np.diff(char_matrix, axis=0) < 0, axis=0))

sol = Solution()
print(f'{sol.minDeletionSize(["abc", "bce", "cae"])} expect 1')
print(f'{sol.minDeletionSize(["cba","daf","ghi"])} expect 1')
print(f'{sol.minDeletionSize(["a","b"])} expect 0')
print(f'{sol.minDeletionSize(["zyx","wvu","tsr"])} expect 3')

# 最適化版のテスト
sol_opt = SolutionOptimized()
print(f'{sol_opt.minDeletionSize(["abc", "bce", "cae"])} expect 1')
print(f'{sol_opt.minDeletionSize(["cba","daf","ghi"])} expect 1')
print(f'{sol_opt.minDeletionSize(["a","b"])} expect 0')
print(f'{sol_opt.minDeletionSize(["zyx","wvu","tsr"])} expect 3')
