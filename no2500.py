class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        grid_list = []
        for g in grid:
            grid_list.append(sorted(g))
        
        num = len(grid_list)
        grid_num = len(grid_list[0])
        total: int = 0
        for i in range(grid_num):
            col_list = []
            for j in range(num):
                col_list.append(grid_list[j][i])
            total += max(col_list)
        return total

sol = Solution()
print(f'{sol.deleteGreatestValue([[1,2,4],[3,3,1]])} expect 8')
print(f'{sol.deleteGreatestValue([[10]])} expect 10')