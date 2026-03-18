from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, acc):
            if not node:
                return acc

            right_sum = dfs(node.right, acc)
            node.val += right_sum
            left_sum = dfs(node.left, node.val)

            return left_sum

        dfs(root, 0)
        return root