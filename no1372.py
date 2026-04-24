from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, left, right):
            if not node:
                return
            self.res = max(self.res, left, right)
            dfs(node.left, 0, left + 1)
            dfs(node.right, right + 1, 0)

        self.res = 0
        dfs(root, 0, 0)
        return self.res