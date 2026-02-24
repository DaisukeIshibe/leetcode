from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        flipped = []
        index = 0
        
        def dfs(node):
            nonlocal index
            if not node:
                return True
            
            if node.val != voyage[index]:
                return False
            
            index += 1
            
            if node.left and node.left.val != voyage[index]:
                flipped.append(node.val)
                node.left, node.right = node.right, node.left
            
            return dfs(node.left) and dfs(node.right)
        
        if dfs(root):
            return flipped
        else:
            return [-1]