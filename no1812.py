class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = coordinates
        a2n_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        # 白ならTrue、黒ならFalse
        col = a2n_dict[x]
        row = int(y)
        return (col + row) % 2 == 1


sol = Solution()
print(f'{sol.squareIsWhite("a1")} expect False')
print(f'{sol.squareIsWhite("h3")} expect True')
print(f'{sol.squareIsWhite("c7")} expect False')
print(f'{sol.squareIsWhite("a2")} expect True')
