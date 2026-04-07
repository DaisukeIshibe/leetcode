from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_diff = 0

        def dfs(node: Optional[TreeNode], current_min: int, current_max: int) -> None:
            if not node:
                return

            current_min = min(current_min, node.val)
            current_max = max(current_max, node.val)

            self.max_diff = max(self.max_diff, current_max - current_min)

            dfs(node.left, current_min, current_max)
            dfs(node.right, current_min, current_max)

        dfs(root, root.val, root.val)
        return self.max_diff