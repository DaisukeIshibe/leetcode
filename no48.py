class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        # 転置
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 各行を反転
        for row in matrix:
            row.reverse()

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = [[7,4,1],[8,5,2],[9,6,3]]
sol.rotate(matrix)
print('No1 ok' if matrix == ans else 'No1 ng')

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
ans = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
sol.rotate(matrix)
print('No2 ok' if matrix == ans else 'No2 ng')