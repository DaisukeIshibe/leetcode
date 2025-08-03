class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        g_len = len(grid)
        local_len = g_len - 2
        out_list = [[0] * local_len for _ in range(local_len)]
        for i in range(local_len):
            for j in range(local_len):
                max_val = float('-inf')
                for k in range(3):
                    for l in range(3):
                        max_val = max(max_val, grid[i + k][j + l])
                out_list[i][j] = max_val
        return out_list

sol = Solution()
grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
ans = [[9,9],[8,6]]
if sol.largestLocal(grid) == ans:
    print("No1. OK")
else:
    print("No1. NG")

grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
ans = [[2,2,2],[2,2,2],[2,2,2]]
if sol.largestLocal(grid) == ans:
    print("No2. OK")
else:
    print("No2. NG")
