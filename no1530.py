from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        def dfs(node, depth):
            if not node:
                return []

            if not node.left and not node.right:
                return [depth]

            left_depths = dfs(node.left, depth + 1)
            right_depths = dfs(node.right, depth + 1)

            for ld in left_depths:
                for rd in right_depths:
                    if ld + rd - 2 * depth <= distance:
                        self.count += 1

            return left_depths + right_depths

        self.count = 0
        dfs(root, 0)
        return self.count