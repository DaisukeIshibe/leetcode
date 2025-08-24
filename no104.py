import sys
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        print("At node:", root.val)
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        current_depth = 1 + max(left_depth, right_depth)
        print("Max depth at node", root.val, "is", current_depth)
        return current_depth