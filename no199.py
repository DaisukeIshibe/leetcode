from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        max_level = 0

        def dfs(node: Optional[TreeNode], level: int):
            nonlocal max_level
            if not node:
                return
            if level > max_level:
                result.append(node.val)
                max_level = level
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 1)
        return result