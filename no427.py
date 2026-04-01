from typing import List
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r1: int, c1: int, r2: int, c2: int) -> Node:
            if r1 > r2 or c1 > c2:
                return None

            is_leaf = True
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if grid[i][j] != grid[r1][c1]:
                        is_leaf = False
                        break
                if not is_leaf:
                    break

            if is_leaf:
                return Node(grid[r1][c1], True, None, None, None, None)

            mid_row = (r1 + r2) // 2
            mid_col = (c1 + c2) // 2
            top_left = build(r1, c1, mid_row, mid_col)
            top_right = build(r1, mid_col + 1, mid_row, c2)
            bottom_left = build(mid_row + 1, c1, r2, mid_col)
            bottom_right = build(mid_row + 1, mid_col + 1, r2, c2)

            return Node(0, False, top_left, top_right, bottom_left, bottom_right)

        n = len(grid)
        return build(0, 0, n - 1, n - 1)