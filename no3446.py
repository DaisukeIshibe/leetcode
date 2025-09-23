class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        flat_list = []
        for g in grid:
            flat_list.extend(g)
        
        len_grid = len(grid)
        diag_list = []
        for i in range(1, len_grid + 1):
            pass
        print(flat_list)
        return []

sol = Solution()
print(f'{sol.sortMatrix([[1,7,3],[9,8,2],[4,5,6]])} expect [[8,2,3],[9,6,7],[4,5,1]]')
print(f'{sol.sortMatrix([[0,1],[1,2]])} expect [[2,1],[1,0]]')