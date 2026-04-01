from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        if not root:
            return []
        
        # Calculate the height of the tree
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        h = height(root)
        w = (1 << h) - 1  # Width of the output matrix
        
        # Initialize the output matrix with empty strings
        res = [["" for _ in range(w)] for _ in range(h)]
        
        # Helper function to fill the matrix
        def fill(node, r, c):
            if not node:
                return
            res[r][c] = str(node.val)
            if r + 1 < h:
                offset = 1 << (h - r - 2)
                fill(node.left, r + 1, c - offset)
                fill(node.right, r + 1, c + offset)
        
        fill(root, 0, (w - 1) // 2)
        return res