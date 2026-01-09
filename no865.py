from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return depth, None
            left_depth, left_node = dfs(node.left, depth + 1)
            right_depth, right_node = dfs(node.right, depth + 1)
            if left_depth > right_depth:
                return left_depth, left_node
            elif right_depth > left_depth:
                return right_depth, right_node
            else:
                return left_depth, node

        return dfs(root, 0)[1]