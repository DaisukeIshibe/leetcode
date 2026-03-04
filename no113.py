from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(node, current_sum, path):
            if not node:
                return
            current_sum += node.val
            path.append(node.val)
            if not node.left and not node.right and current_sum == targetSum:
                result.append(path.copy())
            helper(node.left, current_sum, path)
            helper(node.right, current_sum, path)
            path.pop()

        result = []
        helper(root, 0, [])
        return result