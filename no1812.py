class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = coordinates
        a2n_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        len_grid = len(a2n_dict)
        grid_list = [True] * len_grid * len_grid
        for i in range(len_grid):
            for j in range(len_grid):
                idx = i * len_grid + j
                if i % 2 == 0:
                    if j % 2 == 0:
                        grid_list[idx] = False
                    else:
                        grid_list[idx] = True
                else:
                    if j % 2 == 0:
                        grid_list[idx] = True
                    else:
                        grid_list[idx] = False
        return grid_list[(int(y) - 1) * len_grid + (a2n_dict[x] - 1)]


sol = Solution()
print(f'{sol.squareIsWhite("a1")} expect False')
print(f'{sol.squareIsWhite("h3")} expect True')
print(f'{sol.squareIsWhite("c7")} expect False')
print(f'{sol.squareIsWhite("a2")} expect True')
