from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 0)]
        total_sum = 0

        while stack:
            node, current_sum = stack.pop()
            current_sum = current_sum * 2 + node.val
            
            if not node.left and not node.right:
                total_sum += current_sum
            
            if node.right:
                stack.append((node.right, current_sum))
            if node.left:
                stack.append((node.left, current_sum))

        return total_sum